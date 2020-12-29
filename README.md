# VRCPhotoSorting
VRChatのスクリーンショットフォルダに溜まった写真を日付ごとに仕分けるプログラム

[ダウンロード](https://github.com/Chootana/VRCPhotoSorting/releases/latest)

# How to UseHow to Use
## とりあえず使いたい方へ

1. [こちら](https://github.com/Chootana/VRCPhotoSorting/releases/latest)
からvrc_photo_sorting.zipをダウンロードする

2. 解凍したvrc_photo_sortingフォルダをVRChat(スクショが保存されるフォルダ)と同じ階層に置く

3. ↓このようになればOK（デフォルトではピクチャに置くことになる）
![フォルダ階層例](https://user-images.githubusercontent.com/44863813/103254498-dfaee500-49c8-11eb-8dbe-2141f8ad945f.png)


4. vrc_photo_sorting内のsort_by_day.exeをダブルクリックすると，↓のように写真が日付ごとに仕分けられる．
![仕分け例](https://user-images.githubusercontent.com/44863813/103254726-d2dec100-49c9-11eb-8a36-dd3f1bee434b.png)


5. その後に撮ったスクショは再びVRChatフォルダに溜まっていくため，適宜sort_by_day.exeを実行する


## pythonで実行したい方，自分流にカスタムしたい方へ
1. [こちら](https://github.com/Chootana/VRCPhotoSorting/releases/latest)
からvrc_photo_sorting.zipをダウンロードするかクローンする．

2. フォルダをVRChatフォルダと同じ階層に置く

3. コマンドプロンプトユーザーは該当フォルダ内に移動してsort_by_day.pyを実行
    ```
    C:\[hogehoge]\Pictures\vrc_photo_sorting> python sort_by_day.py
    ```

4. wsl(linux)ユーザーは該当フォルダ内に移動してsort_by_wsl.pyを実行
    ```bash
    /c/[hogehoge]/Pictures/vrc_photo_sorting$ python sort_by_day_wsl.py
    ```
