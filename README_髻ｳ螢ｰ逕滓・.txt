■ 五井ひまわり幼稚園 ナレーション 高品質音源（NanamiNeural）生成キット

【これは何】
報告書サイトのナレーションを、機械音声（暫定）から
高品質な NanamiNeural（女性・自然な日本語）に差し替えるためのキットです。
※クラウド環境ではBing音声がブロックされ高品質生成ができないため、
　ネット接続できるPC（Windows/Mac）で実行していただく方式です。

【同梱物】
- make_audio_nanami.py … 音声生成スクリプト
- narration.json        … ナレーション原稿8本（改訂済み・06はトリプルガード補助金訴求）

【手順】（Windowsの例）
1. Python を入れる（python.org から）。
2. このフォルダでコマンドプロンプトを開く。
3. 次を実行:
      pip install edge-tts
      python make_audio_nanami.py
   → audio フォルダに 01.mp3 〜 08.mp3 ができます。
4. GitHub の goi-himawari-proposal リポジトリで
   「Add file ▸ Upload files」→ できた audio フォルダ（中の8ファイル）を
   audio/ としてアップ（既存があれば上書き）→ Commit。
5. 1〜2分でサイトの音声が高品質版に切り替わります。
   ※ index.html は音声をファイル参照していないため（埋込版）、
     高品質に完全に切り替えるには、別途お渡しする「index.html（高品質埋込版）」に
     差し替えるか、当方で egress 許可後に作り直したものを使ってください。

【声・速さを変えたい】
   python make_audio_nanami.py --voice ja-JP-NanamiNeural --rate +0% --pitch +0Hz
   ほかの声: ja-JP-KeitaNeural（男性）, ja-JP-AoiNeural, ja-JP-MayuNeural

【注意】
- 原稿の金額・効果・補助金は「試算／要確認」。補助金可否は断定していません。
- 困ったら、この環境の egress 許可リストに speech.platform.bing.com を追加いただければ、
  当方（Claude）側で高品質版を生成して一式お渡しできます。
