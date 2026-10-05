import os
import sys
import json
import urllib.request
import urllib.parse
KEYWORDS_DB = {
    "вывод": {
        "en": "Zero-copy I/O, custom ring buffers, kernel-level sys_write, CPU cache-line alignment",
        "zh": "零拷贝 I/O, 自定义环形缓冲区, 内核级 sys_write, CPU 缓存行对齐"
    },
    "текст": {
        "en": "String-view tokenization, SIMD-accelerated parsing, memory-mapped files (mmap), no-allocation text streams",
        "zh": "String-view 分词, SIMD 加速解析, 内存映射文件 (mmap), 零内存分配文本流"
    },
    "память": {
        "en": "Low-level memory management, Working Set optimization, Standby List allocation, RAM cache flushing",
        "zh": "低级内存管理, 工作集优化, Standby List 分配, RAM 缓存刷新"
    },
    "очист": {
        "en": "Garbage collection algorithms, heap defragmentation, proactive memory freeing, process quota management",
        "zh": "垃圾回收算法, 堆碎片整理, 主动内存释放, 进程配额管理"
    },
    "сеть": {
        "en": "Non-blocking asynchronous I/O, epoll/IOCP multiplexing, custom TCP/UDP sockets, zero-copy packets",
        "zh": "非阻塞异步 I/O, epoll/IOCP 多路复用, 自定义 TCP/UDP 套接字, 零拷贝数据包"
    },
    "график": {
        "en": "Hardware-accelerated rendering, GPU pipeline optimization, direct memory compilation, 144 FPS target",
        "zh": "硬件加速渲染, GPU 管线优化, 直接内存编译, 144 FPS 目标帧率"
    },
    "нейро": {
        "en": "Quantization, FP16/INT8 inference, tensor core acceleration, weight optimization, minimal token latency",
        "zh": "量化, FP16/INT8 推理, 张量核心加速, 权重优化, 最小 Token 延迟"
    },
    "ии": {
        "en": "Structured output JSON, deterministic logic, zero hallucinations, reasoning path tracking",
        "zh": "结构化输出 JSON, 确定性逻辑, 零幻觉, 推理路径跟踪"
    },
    "сайт": {
        "en": "Semantic HTML5 layout, vanilla BEM CSS, no-framework JS, hardware acceleration, DOM tree optimization",
        "zh": "语义化 HTML5 布局, 原生 BEM CSS, 无框架 JS, 硬件加速, DOM 树优化"
    },
    "баз": {
        "en": "Query execution path optimization, covering indexes, lock-free transactions, high-concurrency storage blocks",
        "zh": "查询执行路径优化, 覆盖索引, 无锁事务, 高并发存储块"
    },
    "защит": {
        "en": "Static code analysis, buffer overflow protection, memory safety enforcement, anti-tamper constraints",
        "zh": "静态代码分析, 缓冲区溢出保护, 强制内存安全, 防篡改约束"
    }
}
ROLE_TEMPLATES = {
    "1": {"name": "Systems Architect", "base_tech": "Low-Level Kernel Development, Assembly"},
    "2": {"name": "High-Load Backend Engineer", "base_tech": "Distributed Systems, High-Performance Compute"},
    "3": {"name": "UI/UX Principal Frontend", "base_tech": "Hardware-Accelerated Interfaces, Core Engine Rendering"}
}
SYSTEM_INSTRUCTIONS = {
    "en": (
        "Act as a {role}. Expert in {base_tech}.\n"
        "Advanced Core Focus: {smart_tokens}.\n"
        "Rules: Write pure, production-ready, highly optimized code. "
        "Strictly adhere to absolute best practices, zero redundant logic, and strict execution speed."
    ),
    "zh": (
        "扮演 {role}。精通 {base_tech}。\n"
        "核心技术聚焦: {smart_tokens}。\n"
        "架构规则: 编写纯净、生产就绪、高度优化的代码。严格遵循最佳实践，零冗余逻辑，极度追求执行速度效率。"
    )
}
def translate_text(text: str, target_lang: str) -> str:
    try:
        url_encoded = urllib.parse.quote(text)
        url = f"https://googleapis.com{target_lang}&dt=t&q={url_encoded}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            return "".join([part for part in data if part])
    except Exception:
        return text
def generate_smart_tokens(user_input_ru: str, target_lang: str) -> str:
    input_lower = user_input_ru.lower()
    collected_tokens = []
    for key, tokens in KEYWORDS_DB.items():
        if key in input_lower:
            collected_tokens.append(tokens[target_lang])
    if not collected_tokens:
        return "Performance engineering, hardware optimization" if target_lang == "en" else "性能工程, 硬件优化"
    return ", ".join(collected_tokens)
def main():
    if sys.platform == "win32":
        os.system("chcp 65001 > nul")
    print("==================================================")
    print("     PROMPT_FORGE v1.0 // SMART CONTEXT ENGINE    ")
    print("==================================================")
    print("\n[+] Select Specialization:")
    print("  1. Systems Engineer (C / C++ / Kernel / Assembly)")
    print("  2. Backend Architect (Python / Go / High-Load)")
    print("  3. Frontend Principal (HTML / CSS / Clean UI)")
    role_choice = input("> ").strip()
    selected_template = ROLE_TEMPLATES.get(role_choice, ROLE_TEMPLATES["1"])
    print("\n[+] Select Target AI Model Configuration:")
    print("  1. Global Models (ChatGPT, Claude) -> English System Prompts")
    print("  2. Chinese Models (DeepSeek, Qwen) -> Chinese System Prompts")
    model_choice = input("> ").strip()
    target_lang = "zh" if model_choice == "2" else "en"
    print("\n[+] Enter Task Description:")
    user_prompt_ru = input("> ").strip()
    if not user_prompt_ru:
        return
    print("\n[*] Analyzing context and generating contextual engineering tokens...")
    smart_tokens = generate_smart_tokens(user_prompt_ru, target_lang)
    translated_role = translate_text(selected_template["name"], target_lang)
    translated_base_tech = translate_text(selected_template["base_tech"], target_lang)
    translated_user_prompt = translate_text(user_prompt_ru, target_lang)
    system_part = SYSTEM_INSTRUCTIONS[target_lang].format(
        role=translated_role,
        base_tech=translated_base_tech,
        smart_tokens=smart_tokens
    )
    if target_lang == "zh":
        final_prompt = f"【系统指令】\n{system_part}\n\n【用户任务】\n{translated_user_prompt}"
    else:
        final_prompt = f"=== SYSTEM INSTRUCTIONS ===\n{system_part}\n\n=== USER TASK ===\n{translated_user_prompt}"
    print("\n==================================================")
    print(final_prompt)
    print("==================================================")
    input("\n[+] Execution complete. Press [ENTER] to exit...")
if __name__ == "__main__":
    main()
