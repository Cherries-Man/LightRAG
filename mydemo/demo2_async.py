import asyncio


def always_get_an_event_loop():
    try:
        loop = asyncio.get_event_loop()  # 尝试获取当前线程的事件循环
    except RuntimeError:  # 如果当前线程没有事件循环
        loop = asyncio.new_event_loop()  # 创建一个新的事件循环
        asyncio.set_event_loop(loop)  # 将其设为当前线程的事件循环
    return loop


async def async_task():
    print("Async task running!1")
    print("Async task running!2")
    print("Async task running!3")
    print("Async task running!4")


loop = always_get_an_event_loop()  # 获取事件循环
loop.run_until_complete(async_task())  # 运行异步任务，直到完成
