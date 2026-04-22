import sys
import time
import shutil


def ft_tqdm(lst: range):
    """Yield items while displaying a short tqdm-like progress bar."""
    total = len(lst)
    if total == 0:
        return

    start_time = time.time()

    for i, elem in enumerate(lst, start=1):
        columns = shutil.get_terminal_size((80, 20)).columns
        elapsed = time.time() - start_time
        rate = i / elapsed if elapsed > 0 else 0
        remain = (total - i) / rate if rate > 0 else 0
        percent = int(i * 100 / total)
        elapsed_m, elapsed_s = divmod(int(elapsed), 60)
        remain_m, remain_s = divmod(int(remain), 60)
        prefix = f"{percent:3d}%|"
        suffix = (
            f"| {i}/{total} "
            f"[{elapsed_m:02d}:{elapsed_s:02d}<{remain_m:02d}:{remain_s:02d}, "
            f"{rate:.2f}it/s]"
        )
        bar_length = max(1, columns - len(prefix) - len(suffix))
        filled_length = int(bar_length * i / total)
        bar = "█" * filled_length + " " * (bar_length - filled_length)
        line = f"{prefix}{bar}{suffix}"

        sys.stdout.write("\r\x1b[2K" + line)
        sys.stdout.flush()
        yield elem

    # final_percent = 100
    # final_elapsed = time.time() - start_time
    # final_rate = total / final_elapsed if final_elapsed > 0 else 0
    # final_elapsed_m, final_elapsed_s = divmod(int(final_elapsed), 60)
    # final_prefix = f"{final_percent:3d}%|"
    # final_suffix = (
    #     f"| {total}/{total} "
    #     f"[{final_elapsed_m:02d}:{final_elapsed_s:02d}<00:00, {final_rate:.2f}it/s]"
    # )
    # final_columns = shutil.get_terminal_size((80, 20)).columns
    # final_bar_length = max(1, final_columns - len(final_prefix) - len(final_suffix))
    # final_bar = "█" * final_bar_length
    # final_line = f"{final_prefix}{final_bar}{final_suffix}"
    # sys.stdout.write("\r\x1b[2K" + final_line)
    sys.stdout.write("\n")
    # sys.stdout.flush()

    


