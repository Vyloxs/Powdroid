import csv
import matplotlib.pyplot as plt

def file_joule_sum(filename: str) -> float:
    duration = 0
    joules = 0

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            try:
                start_time, end_time, joule = int(line[0]), int(line[1]), float(line[8])
            except Exception as e:
                continue

            if joule < 0:
                break

            duration += end_time - start_time
            joules += joule
    print(f'Durée: {duration / 1000}s, joules: {joules}J')
    return joules

idle1, idle2, idle3 = (file_joule_sum('output/' + x) for x in ['idle1.csv', 'idle2.csv', 'idle3.csv'])
average_idle = sum((idle1, idle2, idle3)) / 3
print(f'Moyenne de la consommation en idle: {average_idle}J')

twitter1, twitter2, twitter3, twitter4, twitter5 = (file_joule_sum(f'output/twitter{x}.csv') for x in range(1, 6))
average_twitter = sum((twitter1, twitter2, twitter3, twitter4, twitter5)) / 5
print(f'Moyenne de la consommation pour Twitter: {average_twitter}J')

reddit1, reddit2, reddit3, reddit4, reddit5 = (file_joule_sum(f'output/reddit{x}.csv') for x in range(1, 6))
average_reddit = sum((reddit1, reddit2, reddit3, reddit4, reddit5)) / 5
print(f'Moyenne de la consommation pour Reddit: {average_reddit}J')

plt.figure()
plt.title("Comparaison de la consommation énergétique moyenne")
plt.bar(['Idle', 'Twitter', 'Reddit'], [average_idle, average_twitter, average_reddit], color=['green', (0, 0.18, 0.29), (0.97, 0.5, 0)])
plt.xlabel("Logiciel (je sais pas trop quoi mettre)")
plt.ylabel("Consommation moyenne (J)")
plt.show()

def power_evolution_graph(filenames, title):
    plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.xlabel('Index du point de mesure')
    plt.ylabel('Consommation (J)')

    for filename in filenames:
        joules_data = []
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for line in reader:
                try:
                    joules = float(line[8])
                    if joules < 0:
                        continue
                    joules_data.append(joules)
                except:
                    continue
        plt.plot(joules_data, label=filename.split('/')[-1])

    plt.legend()
    #plt.grid(True)
    plt.show()

power_evolution_graph(['output/idle1.csv', 'output/idle2.csv', 'output/idle3.csv'], "Évolution de la consommation - Idle")
power_evolution_graph([f'output/twitter{x}.csv' for x in range(1, 6)], "Évolution de la consommation - Twitter")
power_evolution_graph([f'output/reddit{x}.csv' for x in range(1, 6)], "Évolution de la consommation - Reddit")
