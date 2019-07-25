# newcomer-exercise

### DNA配列処理
1. 引数で与えられたDNA配列の逆相補鎖を計算するプログラムを作成せよ
1. 引数として与えられた2つの文字列が逆相補であるかどうかを調べるプログラムを作成せよ
1. FASTA形式のDNA配列データを読み込み、GC含量（GとCの割合）を計算するプログラムを作成せよ
    * DNA配列についてはTSUBAMEの/work1/t2g-IshidaLab/kadai4beginers/以下に21番染色体の先頭のcontig（NT_113952.1.fasta）があるのでそれを利用すること。
1. 配列全体のGC含量だけでなく、ウィンドウ幅w、ステップ幅sでウィンドウ内のGC含量を出力するプログラムを作成し、その結果をプロットするプログラムを作成せよ
 * Pythonを使用する場合はmatplotlibの使用を推奨（Pandasもお薦め）
 * gnuplot, R等外部プログラムの使用も許可するが、自動処理できるようにすること
 * Excelを使用する場合も自動処理は必須
1. GenBank形式のファイルのDNA配列情報をアミノ酸配列に変換して出力するプログラムを作成せよ。また、その結果を/translationのアミノ酸配列情報と比較せよ。
    * GenBANK形式のファイルは/home/usr7/ishida-t-af/kadai4beginers/以下にあるgbpri1.seqを利用すること
1. インターネットを利用してNCBIのサイトから新型インフルエンザウィルス（swine flu, H1N1形） のゲノムHA文節についてgenbank形式のファイルをダウンロードし、上で作成したプログラムを適用し、結果を確認せよ。

### タンパク質構造データ処理
* PDB形式のファイルは/work1/t2g-IshidaLab/share/db/pdb以下のものを利用するか、PDBのサイトから直接ダウンロードすること
* RasmolではなくPyMOLやJmolを使用しても良い（時間のある人は両方試してみること推奨）。


1. RasMolソフトウェアを利用し、ヒトのヘモグロビン（1BUW）の構造を表示せ
    1. チェイン毎に異なる色で表示し、４量体であることを確認せよ
    1. Aチェインだけを表示し、蛋白質鎖をribbon表示し2次構造に従って色付し、また、そこに結合するヘム（HEM）をball and stickによって表示しCPKで色づけせよ。
    1. 上の2つの表示結果をBMP形式で画像として保存せよ

1. PDBファイル名とチェイン名を引数にして、その回転半径（Radius of Gyration）を計算するプログラムを作成せよ。
    * 回転半径は高分子の大きさを示す為に用いられる値で、重心からの平均半径のこと。ここでは全ての原子ではなく、α炭素原子(CA)のみから近似的に計算して良い。
1. 上記のプログラムの結果を利用し、RasMolで重心から回転半径の範囲内にある原子を赤で、範囲外にある原子を青で色づけせよ

### 化合物データ処理
1. RDkitを用いてカノニカルSMILESで表記された下記の化合物の構造式を描き、画像ファイルとして保存せよ。また、下記の化合物の一般名（薬剤名）が何であるか、[ChEMBL](https://www.ebi.ac.uk/chembl)を使って調べよ。また、その際に描画した構造式をサイトの画像と比較し、正しく描画されているか確認せよ。
        Cc1nc(Nc2ncc(s2)C(=O)Nc3c(C)cccc3Cl)cc(n1)N4CCN(CCO)CC4

1. 上記の化合物のMACCS keys Fingerpirntを計算し、その結果を確認せよ

1. 上記の化合物と下記のSDF形式で保存された化合物ライブラリに含まれる全ての化合物の構造の類似度をMACCS keys FingerpirntのTanimoto係数により計算せよ。
   * http://www.cb.cs.titech.ac.jp/~ishida/kadai4beginers/cmpdlib.sdf
   1. 計算された類似度の分布をヒストグラムとして描画せよ
   1. 類似度が0.8以上である化合物と約0.5([0.49,0.51]）である化合物をそれぞれ5個ランダムに選択し、それらの構造式を描画して比較せよ
   1. MACCS keysではなく、FingerprintとしてECFP4を用いた場合について同様の処理を行い、MACCS keysによる結果と比較せよ

### 機械学習入門
この章はscikit-learnの使用を前提としているが、必ずしも使用しなくとも良い
1. UCI Machine Learning RepositoryのIris Data Setについて、花の種類がsetosaかそれ以外（versicolor/virginica）かを判別する予測器を構築せよ（データはscikit-learnであればsklearn.datasetsのload_iris関数で読み込みが可能）
 1. 150あるデータを100の訓練データと50のテストデータに分割せよ 
 1. ロジスティック回帰アルゴリズム(sklearn.linear_model.LogisticRegression)を用いて訓練セットを学習し、テストセットに対して予測を行った時の予測精度を確認せよ
 1. *scikit-learnなどのライブラリを使わずに*、自分でk-最近傍法のアルゴリズムを実装し、テストセットに対する予測精度を(k=1,5,10)でそれぞれ確認せよ

1. 下記のファイルはlibsvmフォーマットで保存されたタンパク質天然変性領域予測のためのデータセットである。各行はタンパク質中のアミノ酸１残基を示し先頭はorder/disorder(+1/-1)を示している。
 * http://www.cb.cs.titech.ac.jp/~ishida/kadai4beginers/disorder.libsvm.dat
 1. このデータセットに対してliner SVMアルゴリズムを用いて予測器を構築し、予測精度を推定せよ。また、予測精度の推定には5-foldのcross validationを行い、精度指標にはQ2 accuracyを利用せよ
 1. 予測精度の確認のためReceiver Operating Characteristic (ROC) curveを描け（ここからがCVを利用せずにデータセットを訓練とテストに２分割してテストデータについて予測精度を確認しても良い）
 1. 予測精度の指標にROCカーブ下面積（AUC）を用いて、liner SVMの学習のハイパーパラメータであるコストパラメータCを最適化し、最適なCとその際のAUCの値を示せ   
