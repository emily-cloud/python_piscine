import sys
import time


def ft_tqdm(lst: range):
    """Yield items while displaying a short tqdm-like progress bar."""
    total = len(lst)
    if total == 0:
        return

    start_time = time.time()
    bar_length = 45

    for i, elem in enumerate(lst, start=1):
        elapsed = time.time() - start_time
        rate = i / elapsed if elapsed > 0 else 0
        remain = (total - i) / rate if rate > 0 else 0
        filled_length = int(bar_length * i / total)
        bar = "█" * filled_length + " " * (bar_length - filled_length)
        percent = int(i * 100 / total)
        elapsed_m, elapsed_s = divmod(int(elapsed), 60)
        remain_m, remain_s = divmod(int(remain), 60)
        line = (
            f"{percent:3d}%|{bar}| {i}/{total} "
            f"[{elapsed_m:02d}:{elapsed_s:02d}<{remain_m:02d}:{remain_s:02d}, "
            f"{rate:.2f}it/s]"
        )

        sys.stdout.write("\r" + line)
        sys.stdout.write(" " * max(0, 80 - len(line)))
        sys.stdout.flush()
        yield elem

    final_percent = 100
    final_bar = "█" * bar_length
    final_line = (
        f"{final_percent:3d}%|{final_bar}| {total}/{total} "
        f"[00:00<00:00, {rate:.2f}it/s]"
    )
    sys.stdout.write("\r" + final_line)
    sys.stdout.write("\n")
    sys.stdout.flush()

    


