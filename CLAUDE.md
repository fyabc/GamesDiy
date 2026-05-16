# SanGuoSha DIY 项目

## 网络工具注意事项

### WebFetch 对中文站点不可用

WebFetch 工具对 bilibili、zhihu、萌娘百科等中文网站会返回 `"Unable to verify if domain is safe to fetch"`。这是 Anthropic 基础设施侧的域名安全验证限制，与本地网络环境、代理配置、底层模型均无关，**无法本地修复**。

**替代方案**：
- 优先使用 **WebSearch** 搜索并汇总信息
- 对于需要抓取全文的场景（尤其是 SPA 站点），让用户直接把内容贴过来
- 普通 HTML 页面可以尝试 `curl`，但 SPA 类站点（bilibili 等）curl 也拿不到有效内容
