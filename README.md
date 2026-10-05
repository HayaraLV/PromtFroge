# ⚙️ PromptForge — Smart Context Prompt Engine (Python)

[RU] Высокопроизводительный CLI-генератор промптов, который анализирует техническое задание, автоматически генерирует Senior-токены архитектуры кода и локализует системные инструкции для раскрытия 100% мощности ИИ-моделей (включая DeepSeek и Claude).

## ✨ Features / Особенности
- **🧠 Heuristic Token Expansion:** Automatically scans text input and injects specific hardware/software terms (e.g., SIMD, Zero-Copy, mmap) based on task context. / **Эвристическое расширение токенов:** автоматически анализирует ТЗ и подбирает жесткие низкоуровневые термины под конкретную задачу.
- **⚡️ DeepSeek & Qwen Native Optimization:** Automatically translates system prompts into native Chinese (`zh`) when targeting Chinese LLMs to trigger maximum reasoning performance. / **Оптимизация под китайские модели:** переводит системные инструкции на китайский язык, заставляя DeepSeek-R1 выдавать максимальный уровень логики.
- **🪶 Zero External Dependencies:** Built entirely using native Python libraries (`urllib`). Lightweight, robust, and works out-of-the-box. / **Ноль зависимостей:** написан на чистом Python без использования тяжелых ломающихся библиотек перевода.
- **🌍 Production-Grade Code Output:** Forces AI models to drop conversational fluff and return pure, hardware-accelerated code. / **Высокое качество кода:** заставляет нейросети убрать «воду» и возвращать чистый, оптимизированный Production-код.

## 🚀 How to Run / Запуск
```bash
python prompt_forge.py
```
