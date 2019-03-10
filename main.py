import lib.opening.py
import lib.menu.py
import lib.get_url.py





if __name__ == '__main__':
    opening_partial, opening_full = build_dict()
    with open("output/opening.txt", "w") as f:
        for key, item in opening_partial.items():
            nbr_win, nbr_match = item
            f.write(key + "-- nombre win: " + str(nbr_win) + "--nombre match: " + str(nbr_match))
            f.write("\n")
