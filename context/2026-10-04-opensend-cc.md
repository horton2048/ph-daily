---
product: opensend.cc
slug: opensend-cc
date: '2026-10-04'
rank: 5
votes: 99
comments: 1
category: 开发者工具
subcategory: 自托管邮件平台
tags:
- 开源
- 邮件
- 自托管
- Resend 替代
- SES
tech_stack:
- Next.js
- Bun
- TypeScript
- PostgreSQL
- AWS SES
- Redis
- Docker
platform:
- Self-host
- Web
- API
open_source: true
license: Elastic License 2.0
business_model: 源码可用自托管 + 托管云早期接入
pricing_start: 自托管免费（付 SES）；云有免费档
funding_stage: 未披露
funding_amount: 未披露
related_products:
- Resend
maker_previous: []
key_signals:
- 源码可用的 Resend 风格邮件平台，跑在自有服务器 + AWS SES
- Elastic License 2.0：可自托管，不可转售为竞品托管服务
- Docker Compose 一键起；云版 opensend.namuh.co 早期接入
archived_at: '2026-10-04T21:20:00+08:00'
sources_count: 3
---

# opensend.cc · 扩展阅读上下文

> PT 2026-10-04 Product Hunt 榜单第 5 · 👍 99 · 💬 1  
> 归档日期 2026-10-04 · 本文档为事实性扩展阅读，不含观点判断

## 基本信息

| 字段 | 值 |
|---|---|
| 产品名 | opensend.cc / OpenSend |
| 英文 tagline | The open source email platform that runs on your server |
| 中文 tagline | 跑在自己服务器上的开源邮件平台 |
| 官网 | https://opensend.namuh.co （云）；文档与自托管指南同域；仓库 https://github.com/namuh-eng/opensend |
| PH 页 | https://www.producthunt.com/products/opensend-cc |
| 品类标签 | Email · Open Source · Developer Tools |
| 票数 / 评论 | 99 / 1 |
| 公司主体 | Namuh（README：Built by Jaeyun Ha and Ashley Ha） |
| 企业版/关联站点 | Cloud: opensend.namuh.co ；GHCR 镜像 v1.0.0 |

## 是做什么的（如实复述，不评价）

OpenSend 是自托管邮件基础设施：REST API、SDK、React 邮件模板、域名验证、Webhook、广播、自动化、分析与管理后台。自托管部署使用你自己的 AWS SES 配额与基础设施；默认 Compose 栈宣称不向 OpenSend/Namuh/Sentry/PostHog 等「打电话」除非显式配置。协议为 Elastic License 2.0。另有早期接入的 OpenSend Cloud。

## 解决什么问题（事实层面，不判断值不值得解）

- 想要熟悉的邮件 API/仪表盘，但数据与密钥留在自有边界
- 想用自家 SES 配额并检查完整发送链路
- 托管邮件 SaaS 无法满足数据驻留或供应商锁定顾虑

## 怎么做的（技术原理/机制，事实层面）

- `bun run setup && docker compose up -d`：Postgres、Redis、app(:3015)、ingester(:3016)、scheduler 等
- 技术栈：Next.js 16、Bun、Drizzle、Better Auth、Hono ingester、SES v2、可选 SMTP relay
- SDK：TypeScript / Python / Go / Ruby
- Webhook：HMAC、Svix 兼容头
- 文档含 llms.txt、OpenAPI、MCP 指引

## 团队 / 背景 / 融资

| 字段 | 值 | 来源 |
|---|---|---|
| 创始人 | Jaeyun Ha、Ashley Ha | GitHub README |
| 融资 | 未查到 | |
| GitHub stars | 约 43（抓取时） | GitHub |

## 定价 / 商业模式

- 自托管：软件免费（ELv2）；自付 SES/基础设施
- Cloud：早期接入；Free 档无需绑卡；付费经 Stripe（细节价目未在本次抓取中完整展开）

## 关联信息 / 生态

定位为「open source Resend alternative」。注意：opensend.com 是另一家 DTC 访客识别产品，勿混淆。

## 技术时间线

| 日期 | 事件 |
|---|---|
| 2026-03 | 仓库创建摘要 |
| v1.0.0 | 发布固定 GHCR 镜像与 Compose 标签 |
| 2026-10-04 | 登 PH 日榜第 5 |

## 评论区反馈

PH 仅 1 条评论；本次未抓取原文。

## 信息来源

- https://github.com/namuh-eng/opensend （README）
- opensend.namuh.co 文档摘要 / self-hosting 摘要
- Product Hunt / UIComet 发布摘要

## 未查到 / 待补

- Cloud 完整价目表
- opensend.cc 域名与 namuh.co 的精确跳转关系
- 融资信息
