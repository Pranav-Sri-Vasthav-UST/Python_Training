path = r"D:\Python Training\Python_Training\04_03\students.csv"
try:
    f = open(path)
    content = f.readlines()
    f.close()
    all_list = []
    header_list = []


    for line in content:
        all_list.append(line.strip('\n'))

    all_list = [lists.split(',') for lists in all_list]

    for lists in all_list:
        if lists[0] == 'name':
            header_list = lists
            for i, column_name in enumerate(header_list):
                globals()[f'list{i+1}'] = []

    for i, row in enumerate(all_list[1:]):
        for j, value in enumerate(row):
            globals()[f'list{j+1}'].append(value)

    avg_list = []
    for i in range(len(list3)):
        scores = list(map(int, [list4[i], list5[i], list6[i], list7[i]]))
        avg = sum(scores) / len(scores)
        avg_list.append(avg)
        list8[i] = avg

    unique_avgs = sorted(set(avg_list), reverse=True)

    avg_to_rank = {avg: i+1 for i, avg in enumerate(unique_avgs)}



    for i in range(len(avg_list)):
        list9[i] = avg_to_rank[avg_list[i]]

    student_dict = {}
    for i in range(len(list3)):
        student_data = [globals()[f'list{j+1}'][i] for j in range(len(header_list))]
        student_dict[list3[i]] = student_data

    print("Student Dictionary with regid as key:")
    for key, value in student_dict.items():
        print(f"{key}: {value}")

    with open(r"D:\Python Training\Python_Training\04_03\student_rank.txt", "w") as file:
        file.write('-' * 68 + '\n')
        file.write('|'.join(h.ljust(7) for h in header_list) + '\n')
        file.write('-' * 68 + '\n')
        
        for value in student_dict.values():
            file.write('|'.join(str(v).ljust(7) for v in value) + '\n')
        
        file.write('-' * 68 + '\n')
    
    with open(r"D:\Python Training\Python_Training\04_03\student_rank.txt", "a") as file:
        file.write('\n\nSorted by Rank:\n')
        file.write('-' * 68 + '\n')
        file.write('|'.join(h.ljust(7) for h in header_list) + '\n')
        file.write('-' * 68 + '\n')
        
        sorted_students = dict(sorted(student_dict.items(), key=lambda item: item[1][8]))
        
        for value in sorted_students.values():
            file.write('|'.join(str(v).ljust(7) for v in value) + '\n')
        
        file.write('-' * 68 + '\n')
    
    with open(r"D:\Python Training\Python_Training\04_03\student_rank.csv", "w") as file:
        file.write(','.join(header_list) + '\n')
        for value in student_dict.values():
            file.write(','.join(map(str, value)) + '\n')

except FileNotFoundError:
    print(f"Error: File not found at {path}")
except Exception as e:
    print(f"An error occurred: {e}")