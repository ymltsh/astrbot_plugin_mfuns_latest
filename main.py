import aiohttp
from astrbot.api.all import *

API_URL = "https://mfuns.wgen.top/llm/latest"


class MfunsLatestPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @command("mfuns")
    async def mfuns(self, event: AstrMessageEvent, type: str = "all", limit: int = 10):
        """获取 MFuns 最新内容

        Args:
            type: 内容类型，可选 all/feed/video/article，默认 all
            limit: 返回数量，默认 10，最大 100
        """
        limit = max(1, min(limit, 100))
        valid_types = {"all", "feed", "video", "article"}
        if type not in valid_types:
            yield event.plain_result(
                f"类型参数错误，允许的值: {', '.join(valid_types)}"
            )
            return

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    API_URL,
                    params={
                        "type": type,
                        "limit": limit,
                        "format": "markdown",
                    },
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as resp:
                    resp.raise_for_status()
                    text = await resp.text()
                    yield event.plain_result(text)
        except Exception as e:
            yield event.plain_result(f"MFuns 查询失败: {e}")

    @llm_tool("mfuns_latest")
    async def mfuns_latest_tool(
        self, event: AstrMessageEvent, type: str = "all", limit: int = 10
    ):
        """获取 MFuns（喵御宅/M站）最新内容，包括动态(feed)、视频(video)和文章(article)。

        当用户询问 MFuns 最近有什么更新、最新视频、最新文章、最新动态、最近发布内容时使用此工具。

        Args:
            type: str
                内容类型。可选值: all(全部), feed(动态), video(视频), article(文章)。默认 all。
            limit: int
                返回数量。默认 10，最大 100。
        """
        limit = max(1, min(limit, 100))
        valid_types = {"all", "feed", "video", "article"}
        if type not in valid_types:
            return f"类型参数错误，允许的值: {', '.join(valid_types)}"

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    API_URL,
                    params={
                        "type": type,
                        "limit": limit,
                        "format": "markdown",
                    },
                    timeout=aiohttp.ClientTimeout(total=30),
                ) as resp:
                    resp.raise_for_status()
                    return await resp.text()
        except Exception as e:
            return f"MFuns 查询失败: {e}"
