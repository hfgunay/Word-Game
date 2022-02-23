import sys
import time

if len(sys.argv) != 3:
    print("You must write two arguments for this program")


with open(sys.argv[1],"r",encoding="utf-8") as file1:

    with open(sys.argv[2],"r",encoding="utf-8") as file2:
        harf = dict()
        kelimeler = dict()
        for line in file2:
            line = line.rstrip("\n")
            argumans = line.split(":")
            harf[argumans[0]] = argumans[1]
        for line2 in file1:
            line2 = line2.rstrip("\n")
            liste = line2.split(":")
            kelimeler[liste[0]] = dict()
            kelimeler[liste[0]] = liste[1]
            kelimeler.keys()
        temp_dict = dict()
        karisik_kelimeler = list()
        for i in kelimeler.keys():
            temp_dict[i] = list()
            karisik_kelimeler.append(i)
            for j in kelimeler[i].split(","):
                temp_dict[i].append(j)


            u = 0

        max_time = 30
        while u < len(karisik_kelimeler):
            starting_time = time.time()
            toplam_puan = 0
            print("Shuffled letters are: {} Please guess words for these letter with minimum three letters".format(karisik_kelimeler[u]))
            guessed_words = list()
            while True:
                guess = input("Guessed Word:")
                guess = guess.replace("i","İ")
                time_left = max_time-(time.time()-starting_time)
                if guess in guessed_words:
                    print("This word is guessed before")
                    print("You have {} time".format(int(time_left)))

                    continue
                if int(time_left) >0:
                    print("You have  {}  time".format(int(time_left)))

                else:
                    if len(guessed_words) == 0:
                            print("Score for {} is 0 and no words guessed were guessed.".format(karisik_kelimeler[u],end=""))
                    else:
                        print("You have 0 time")
                        print("Score for {} is {} and the guessed words are ".format(karisik_kelimeler[u],str(toplam_puan)),end="")
                    for k in guessed_words:
                        if k == guessed_words[-1]:
                            print("{}".format(k),end="")
                        else:
                            print("{}-".format(k),end="")
                    print()
                    break
                counter_for_valid_words = 0
                for kelime in temp_dict[karisik_kelimeler[u]]:
                    if guess.upper() == kelime.upper():
                        counter_for_valid_words += 1
                        puan = 0
                        for harf1 in kelime:
                            for harf2 in harf.keys():
                                if harf1 == harf2:
                                    puan += int(harf[harf2])
                        puan = puan * len(kelime)
                        if guess not in guessed_words:
                            guessed_words.append(guess.upper())

                        toplam_puan += puan
                    else:
                        pass
                if counter_for_valid_words == 0:
                    print("Your guessed word is not valid word")
            u += 1
            if u == len(karisik_kelimeler):
                print("Game is over.")

