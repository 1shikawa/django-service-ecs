# worklog management
<h2>概要</h2>
担当者がどの案件作業にどの程度時間をかけているのかを管理者が数値的かつ視覚的に把握できるアプリ<br>
運用環境（AWS）：https://worklog-management.ml<br>
管理サイト（AWS）：https://worklog-management.ml/admin

<h2>機能一覧</h2>
<ul>
    <li>ユーザ登録、認証機能</li>
    <li>ユーザパスワード変更、再設定機能</li>
    <li>カレンダー表示機能</li>
    <li>年月日単位での作業ログ複数登録、更新機能</li>
    <li>登録者の入力一覧表示機能</li>
    <li>登録者毎の日次集計機能</li>
    <li>登録者毎の月次集計機能</li>
    <li>登録者毎の項目別円グラフ表示機能</li>
    <li>単体テスト機能</li>
</ul>

<h2>利用技術一覧</h2>
<ul>
    <li>言語/フレームワーク
    <ul>
        <li>Python3.7/Django2.1</li>
        <li>Javascript</li>
        <li>Bootstrap4</li>
    </ul>
    </li>
    <li>開発環境
    <ul>
        <li>PycharmPro,VisualStudioCode</li>
        <li>Git,Github</li>
        <li>Docker,Docker-Compose</li>
    </ul>
    </li>
    <li>デプロイ運用環境
    <ul>
        <li>Terraform</li>
        <li>CircleCI</li>
        <li>AWS VPC,ECS,EC2,ELB,Route53,S3,RDS等</li>
        <li>SendGrid</li>
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
    <li>テストフレームワーク
    <ul>
        <li>Pytest</li>
    </ul>
    </li>
    <li>グラフ作成
    <ul>
        <li>Chart.js</li>
    </ul>
    </li>
</ul>

<h2>システム構成</h2>
TBD
