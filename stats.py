def word_count(readfile):
        word_split = readfile.split()
        word_count = len(word_split)
        return word_count


def character_counts(book_text):
        lower = book_text.lower()
        count_dict = {}
        for char in lower:
            if char in count_dict:
                   count_dict[char] += 1
            else:
                count_dict[char] = 1
        return count_dict


def sort_on(dictionary):
      return dictionary["num"]
      


def fancy_report (char_count):
      pre_sorted=[]
      for key, value in char_count.items():
            item = {"char": key, "num": value}
            pre_sorted.append(item)
      pre_sorted.sort(reverse=True, key=sort_on)
      return pre_sorted

