<<<<<<< HEAD
# Telegram 每日签到（个人号，纯云端）

这个模板用于给 Telegram 机器人会话每天发送一条签到消息。

## 目录

- `send_sign.py`: 定时发送签到消息
- `generate_session.py`: 一次性生成 `TG_SESSION`
- `.github/workflows/telegram-sign.yml`: GitHub Actions 定时任务

## 1. 准备 Telegram API

去 `https://my.telegram.org` 登录你的手机号账号，创建应用后拿到：

- `api_id`
- `api_hash`

## 2. 在 GitHub 仓库设置 Secrets

仓库 -> `Settings` -> `Secrets and variables` -> `Actions`，新增：

- `TG_API_ID`: 你的 `api_id`
- `TG_API_HASH`: 你的 `api_hash`
- `TG_TARGET`: 目标机器人用户名，如 `@xxx_bot`
- `TG_SIGN_TEXT`: 签到文本，如 `签到`
- `TG_SESSION`: 先留空，下一步生成后再填

## 3. 纯云端一次性生成 TG_SESSION

推荐用 GitHub Codespaces（浏览器里完成，不需要本地环境）：

1. 仓库页面点击 `Code` -> `Codespaces` -> `Create codespace on main`
2. 在 Codespaces 终端执行：

```bash
pip install -r requirements.txt
export TG_API_ID='你的api_id'
export TG_API_HASH='你的api_hash'
python generate_session.py
```

3. 按提示输入手机号、验证码、二步密码（如有）
4. 复制终端输出的长字符串，保存为 GitHub Secret: `TG_SESSION`

## 4. 测试执行

进入仓库 `Actions`，手动运行 `Telegram Daily Sign (User Account)`。
看到成功日志后，去目标机器人会话确认是否收到签到消息。

## 5. 定时规则说明

工作流当前设置：

- `cron: "0 0 * * *"`（UTC 时间）
- 对应中国时区（Asia/Shanghai）每天 `08:00`

如果你要改时间，修改 `.github/workflows/telegram-sign.yml` 的 `cron` 即可。

## 注意事项

- `TG_SESSION` 等同登录凭证，只能放在 GitHub Secrets，不能写进代码。
- Telegram 可能触发风控，建议固定时间、固定内容，不要高频发送。
=======
# whw
WO DE CANG KU
>>>>>>> ce8fb1c8202e972bd905f7acf9e3250686b50ea0
