# worklog management
<h2>概要</h2>
担当者がどの案件作業にどの程度時間をかけているのかを管理者が数値的かつ視覚的に把握できるアプリ\
運用環境（AWS）：https://worklog-management.ml\
管理サイト（AWS）：https://worklog-management.ml/admin


# 機能一覧
<ul>
    <li>ユーザー認証・メール認証</li>
    <li>記事一覧表示機能</li>
    <li>記事詳細表示機能</li>
    <li>記事投稿機能</li>
    <li>管理ユーザ登録機能</li>
    <li>管理ユーザログイン機能</li>
    <li>画像ファイルのアップロード機能</li>
    <li>DBテーブルのリレーション管理</li>
    <li>DBトランザクションの制御機能</li>
    <li>ページネーション機能</li>
    <li>単体テスト機能</li>
    <li>統合テスト機能</li>
</ul>

# 利用技術一覧
<ul>
    <li>言語/フレームワーク
    <ul>
        <li>Python3.7/Django2.1</li>
        <li>Javascript<li>
        <li>Bootstrap4</li>
    </ul>
    </li>
    <li>開発環境
    <ul>
        <li>PycharmPro,VSCode,Git(GitHUB)</li>
        <li>Docker(Compose)</li>
    </ul>
    </li>
    <li>デプロイ運用環境
    <ul>
        <li>Terraform</li>
        <li>CircleCI</li>
        <li>AWS VPC,ECS,EC2,ELB,Route53,S3,RDS等</li>
    </ul>
    </li>
    <li>Web(wsgi)サーバ
    <ul>
        <li>nginx/gunicorn</li>
    </ul>
    <li>DB
    <ul>
        <li>(開発環境)MySQL5.7</li>
        <li>(運用環境)AWSRDS MySQL5.7</li>
    </ul>
    </li>
    <li>テスト
    <ul>
        <li>Pytest</li>
    </ul>
    </li>
    <li>グラフ作成
    <ul>
        <li>Chart.js</li>
    </ul>
    </li>
    <li>各種DBリレーション</li>
</ul>

# システム構成
TBD