ign = input("In-game name (IGN): ")
rank = input("Current rank: ")

hero_names = ["Layla", "Tigreal", "Gusion", "Kagura", "Chou"]
hero_roles = ["Marksman", "Tank", "Assassin", "Mage", "Fighter"]

print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

for i in range(len(hero_names)):
    print(f" {i+1}. {hero_names[i]:10} [{hero_roles[i]}]")

print("==========================================")

match_logs = []
wins = 0
losses = 0
best_kda = 0
best_match = ""

for match in range(1, 5):
    print(f"\n--- MATCH {match} ---")
    hero_number = int(input("Hero number (0 to skip): "))

    if hero_number == 0:
        continue

    if 1 <= hero_number <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()

        denominator = deaths if deaths != 0 else 1
        kda = (kills + assists) / denominator

        if kda >= 5 and result == "W":
            tag = "DOMINATION!"
        elif kda >= 5 and result == "L":
            tag = "Carried Hard"
        elif kda < 5 and result == "W":
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        if result == "W":
            wins += 1
            result_text = "WIN"
        else:
            losses += 1
            result_text = "LOSS"

        hero_name = hero_names[hero_number - 1]

        match_logs.append([hero_name, kda, result_text, tag])

        if kda > best_kda:
            best_kda = kda
            best_match = hero_name

matches_played = len(match_logs)
win_rate = int((wins / matches_played) * 100) if matches_played > 0 else 0

print("\n=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for i in range(len(match_logs)):
    print(f"[{i+1}] {match_logs[i][0]:10} | "
          f"KDA: {match_logs[i][1]:.2f} | "
          f"{match_logs[i][2]:4} | "
          f"{match_logs[i][3]}")

print("---------------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")
print(f"Best Match     : {best_match} (KDA: {best_kda:.2f})")
print("=============================================")
