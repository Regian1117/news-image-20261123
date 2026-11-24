// A working news-image-daily entry (Node 22, standard library only): its image is the entry.png beside this file, and
// the program copies it to /output/entry.png. A starting point, not a winner: replace the image. The gate takes a
// whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { createHash } from 'node:crypto';
import { copyFileSync, existsSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const MAX_BYTES = 1_048_576;
const MAX_DIM = 1024;
const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);

interface PngInfo {
  width: number;
  height: number;
  bytes: number;
  sha256: string;
}

function sha256Hex(buf: Buffer): string {
  return createHash('sha256').update(buf).digest('hex');
}

function validateSourcePng(sourceUrl: URL): PngInfo {
  if (!existsSync(sourceUrl)) {
    throw new Error('Missing source image: ./entry.png');
  }
  const buf = readFileSync(sourceUrl);
  if (buf.length < 24) {
    throw new Error(`Invalid PNG: file too small (${buf.length} bytes)`);
  }
  if (buf.length > MAX_BYTES) {
    throw new Error(`PNG exceeds 1 MiB cap: ${buf.length} > ${MAX_BYTES} bytes`);
  }
  if (!buf.subarray(0, 8).equals(PNG_MAGIC)) {
    throw new Error('Invalid PNG: magic bytes mismatch');
  }
  const chunkType = buf.subarray(12, 16).toString('ascii');
  if (chunkType !== 'IHDR') {
    throw new Error(`Invalid PNG: expected IHDR chunk, found ${chunkType}`);
  }
  const width = buf.readUInt32BE(16);
  const height = buf.readUInt32BE(20);
  if (width < 1 || height < 1 || width > MAX_DIM || height > MAX_DIM) {
    throw new Error(`Invalid PNG dimensions: ${width}x${height} (max ${MAX_DIM}x${MAX_DIM})`);
  }
  return { width, height, bytes: buf.length, sha256: sha256Hex(buf) };
}

const sourceUrl = new URL('./entry.png', import.meta.url);
const srcInfo = validateSourcePng(sourceUrl);

const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outputDir, { recursive: true });
const destPath = join(outputDir, 'entry.png');
copyFileSync(sourceUrl, destPath);

const destBuf = readFileSync(destPath);
const destSha256 = sha256Hex(destBuf);
if (destBuf.length !== srcInfo.bytes || destSha256 !== srcInfo.sha256) {
  throw new Error(
    `Output verification failed: bytes ${destBuf.length}/${srcInfo.bytes}, sha256 ${destSha256}/${srcInfo.sha256}`,
  );
}

console.log(
  JSON.stringify({
    status: 'ok',
    output: destPath,
    width: srcInfo.width,
    height: srcInfo.height,
    bytes: destBuf.length,
    sha256: destSha256,
  }),
);
