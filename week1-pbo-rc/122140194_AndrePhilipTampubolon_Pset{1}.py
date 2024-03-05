class Hero:
    def __init__(self, name, hp, armor, attack):
        self.name = name
        self.hp = hp
        self.base_armor = armor  # Menambah atribut base_armor untuk menyimpan armor awal
        self.armor = armor
        self.attack = attack
        self.is_defending = False  # Status bertahan
        self.is_active = True  # Status aktif (belum menyerah)

    def take_damage(self, amount):
        # HP Hero berkurang setelah menerima damage
        damage_taken = amount
        if self.is_defending:
            # armor yang bakalan berkurang dulu jika mode bertahan
            if damage_taken > self.armor:
                damage_taken -= self.armor
                self.armor = 0
            else:
                damage_taken = 0
            # mengurangi armor setelah dipakai ketika mode bertahan
            self.armor -= self.base_armor // 2  # jika lawan menyerang dan kita mode bertahan, bakalan ngurangi armor setengah
            self.armor = max(0, self.armor)  # memastikan armor tidak negatif walaupun serangan > armor

        self.hp -= damage_taken
        if self.hp < 0:
            self.hp = 0  # memastikan agar hp tidak kurang dari 0

    def attack_enemy(self, enemy):
        # Menyerang musuh
        if self.is_active and enemy.is_active:  # Memeriksa apakah hero aktif dan musuh aktif
            print(f"{self.name} menyerang {enemy.name}!")
            enemy.take_damage(self.attack)

    def defend(self):
        # Bertahan
        self.is_defending = True
        print(f"{self.name} sedang bertahan.")

    def end_defense(self):
        # Berhenti bertahan
        self.is_defending = False
        self.armor = self.base_armor  # Mengembalikan armor ke nilai awal setelah berhenti bertahan
        print(f"{self.name} berhenti bertahan.")

    def surrender(self, enemy):
        # Menyerah
        self.is_active = False
        print(f"{self.name} menyerah. {enemy.name} Menang!")
    
    def info_hero(self):
        print(f"Name : {self.name}, HP = {self.hp}, Armor : {self.armor}, Attack : {self.attack}")


class Match:
    def __init__(self, selected_heroes):
        self.selected_heroes = selected_heroes
        self.turn = 1  # Inisialisasi giliran
        self.hero1 = None  # Inisialisasi objek hero1
        self.hero2 = None  # Inisialisasi objek hero2
    
    def switch_turn(self):
        # Mengganti giliran
        self.turn = 2 if self.turn == 1 else 1

    def infoMatch(self, heroes):
        for i, selected_hero_name in enumerate(self.selected_heroes):
            print(f"Hero yang ingin Anda {'pakai' if i == 0 else 'lawan'}:")
            found = False
            for hero in heroes:
                if hero.name == selected_hero_name:
                    hero.info_hero()
                    found = True
                    if i == 0:
                        self.hero1 = hero  # Menyimpan objek hero1
                    else:
                        self.hero2 = hero  # Menyimpan objek hero2
                    break
            if not found:
                print(f"Hero {selected_hero_name} tidak ditemukan.")
            print()
    
    def matchStarted(self):
        print("=== Mulai Pertandingan ===")
        while self.hero1.is_active and self.hero2.is_active:
            current_hero = self.hero1 if self.turn == 1 else self.hero2
            enemy_hero = self.hero2 if self.turn == 1 else self.hero1

            print(f"Giliran {current_hero.name}:")
            action = input("Tindakan (serang/bertahan/menyerah): ").lower()

            if action == "serang":
                current_hero.attack_enemy(enemy_hero)
                current_hero.info_hero()
                enemy_hero.info_hero()
            elif action == "bertahan":
                current_hero.defend()
            elif action == "menyerah":
                current_hero.surrender(enemy_hero)
                break  # Keluar dari loop jika hero menyerah
            else:
                print("Aksi tidak valid. Silakan pilih 'serang', 'bertahan', atau 'menyerah'.")

            # Periksa apakah HP lawan telah mencapai 0 atau kurang
            if enemy_hero.hp <= 0:
                print(f"{enemy_hero.name} telah kalah! {current_hero.name} Menang!")
                break

            self.switch_turn()

        print("=== Pertandingan Selesai ===")

if __name__ == "__main__":  
    list_heroes = [["ling", 100, 25, 35], ["alucard", 100, 50, 25], ["lolita", 100, 75, 15], ["change",100,20,30]]
    heroes = []  
    list_SelectedHeroes = []

    # Membuat objek Hero dan menyimpannya dalam list heroes
    for dataHero in list_heroes:
        hero = Hero(*dataHero)  
        heroes.append(hero)

    print("\nSelamat Datang Pada Pertandingan Duel Hero Mobile Legend\n")
    print("Daftar Hero : ")
    for hero in heroes:
        hero.info_hero()
    print(" ")
    
    # Memilih hero
    for i in range(2):
        if i == 0:
            heroes_selected = input(f"Pilih hero yang ingin Anda pakai: ")
            list_SelectedHeroes.append(heroes_selected)
        else:
            heroes_selected = input(f"Pilih hero yang ingin Anda lawan: ")
            list_SelectedHeroes.append(heroes_selected)
    print(" ")

    # Membuat objek Match dan memanggil method infoMatch()
    match = Match(list_SelectedHeroes)
    match.infoMatch(heroes)
    match.matchStarted()
