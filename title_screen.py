import curses
import time


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(False)
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    title = "MY AWESOME GAME"
    instruction = "Press any key to start..."

    x_title = (w // 2) - (len(title) // 2)
    x_instr = (w // 2) - (len(instruction) // 2)

    stdscr.addstr(h // 2, x_title, title, curses.A_BOLD)
    stdscr.addstr(h // 2 + 2, x_instr, instruction)
    stdscr.refresh()

    stdscr.getch()

    stdscr.clear()
    stdscr.addstr(h // 2, (w // 2) - len("Game Starting...") // 2, "Game Starting...")
    stdscr.refresh()
    time.sleep(1)


if __name__ == "__main__":
    curses.wrapper(main)
