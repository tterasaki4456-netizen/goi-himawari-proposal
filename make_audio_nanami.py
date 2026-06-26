#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
五井ひまわり幼稚園 ナレーション 高品質音源生成（NanamiNeural / Edge TTS）

同じフォルダの narration.json を読み、ja-JP-NanamiNeural で audio/01-08.mp3 を生成します。
※ネットに接続できるPCで実行してください（Edge TTS はオンライン合成）。

使い方:
  pip install edge-tts
  python3 make_audio_nanami.py
  → ./audio/01.mp3 ... 08.mp3 が出力されます。
  → できた audio フォルダを GitHub の goi-himawari-proposal リポジトリに
     「audio/」として Upload（既存があれば上書き）すれば、サイトが高品質音声に切り替わります。

声・速度を変えたい場合:
  python3 make_audio_nanami.py --voice ja-JP-NanamiNeural --rate +0% --pitch +0Hz
  （他の声例: ja-JP-KeitaNeural=男性 / ja-JP-AoiNeural / ja-JP-MayuNeural）
"""
import argparse, asyncio, json, os, sys

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="ja-JP-NanamiNeural")
    ap.add_argument("--rate", default="+0%")
    ap.add_argument("--pitch", default="+0Hz")
    ap.add_argument("--json", default="narration.json")
    ap.add_argument("--out", default="audio")
    args = ap.parse_args()

    try:
        import edge_tts
    except ImportError:
        sys.exit("edge-tts が未インストールです。先に `pip install edge-tts` を実行してください。")

    nar = json.load(open(args.json, encoding="utf-8"))
    os.makedirs(args.out, exist_ok=True)

    async def synth(text, path):
        c = edge_tts.Communicate(text, args.voice, rate=args.rate, pitch=args.pitch)
        await c.save(path)

    async def run():
        for n in nar:
            fn = n.get("file") or ""
            text = (n.get("text") or "").strip()
            if not fn or not text:
                continue
            path = os.path.join(args.out, fn)
            await synth(text, path)
            print(f"  生成: {args.out}/{fn}  ({n.get('title','')})")

    asyncio.run(run())
    print("完了。audio フォルダを GitHub の goi-himawari-proposal に上書きアップしてください。")

if __name__ == "__main__":
    main()
