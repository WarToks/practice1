夏季休業期間に学習したことの記録用のメモかつmarkdownの練習

# Javascript 編

実行に関していくつか方法はあるが今回は`.html`ファイルと`.js`ファイルを別個に用意するやり方について


- `.html`の名前を`practice.html`, `.js`ファイルの名前を`pr.js`として今回は扱う.

1. `practice.html`として以下の内容を保存する

    ``` html:practice.html
    <!DOCTYPE html>
    <html lang = 'ja'>
    <head>
      <title> タイトル名 </title> <!-- ① -->
      <meta charset="UTF-8"> 
    </head>
    <body>
      <script src = pr.js> </script> <!-- ② -->
    </body>
    </html>
    ```

   - ① は表示するタイトルの名前である.

   - ② において, `<script src = pr.js>`の部分に関して, `pr.js`の相対パスまたは絶対パスを通している.
   
   - `<!-- コメント -->` と`.html`ファイルに記述することでコメントができる
   
 2. `pr.js`に命令を書く
 
 3. `practice.html` をSafariやChromeブラウザに貼り付けて実行!!!!!

# Javascriptについて

## コメントや文末について 
- C/C++言語のように コメントは `// `や`/* */` でやればいい！
- 文末は`;`をつける必要がある
- pythonのようにインデントは無視される
<br />

## ポップアップを表示する方法

- `alert(文字列)` を用いればよい！！！
    
    ```js
    alert("これは文字列です");
    ```

    #### 結果

    ![2018-08-28 1 37 43](https://user-images.githubusercontent.com/34710586/44672316-078d8700-aa63-11e8-8bbc-2ac1af5195b7.png)
    
## htmlファイルに記述する方法

- `document.write()`メソッドを用いる.

   ```js
   document.write("ほげほげ");
   ```



