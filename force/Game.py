import os
from fuck.Map import Map


class Game:
    def __init__(self):
        self.map = Map()

        # スタート時のprinceの位置座標の取得
        prince_location = [(room.x, room.y) for floor_y in self.map.floor for room in floor_y if room.prince]
        self.prince_location_x = prince_location[0][0]
        self.prince_location_y = prince_location[0][1]

        # スタート時のroomObjの参照
        self.room = self.map.room(self.prince_location_x, self.prince_location_y)

    def move_prince(self, diff_x, diff_y):
        # 座標の差分を引数として取って移動をする

        # 戻り値の入れ物
        message = ''

        # 差分を計算した座標
        x = self.prince_location_x + diff_x
        y = self.prince_location_y + diff_y

        # 現在のroomオブジェクトの取得
        now_room = self.map.room(self.prince_location_x, self.prince_location_y)
        # 移動先のroomオブジェクトの取得
        new_room = self.map.room(x, y)

        # 移動先の部屋が存在するとき
        if new_room and not new_room.is_locked:
            # princeオブジェクトの取得
            prince = now_room.prince

            # 移動先の部屋に swordがあった場合
            if new_room.is_sword:
                prince.sword_equip()
                self.map.room(x, y, 'sword')
                message += 'sword equip!\n'

            # 新しい部屋にprinceを配置
            self.map.room(x, y, set_prince=prince)
            # 今いる部屋からprinceを削除
            self.map.room(self.prince_location_x, self.prince_location_y, 'prince')
            # 新しい部屋を訪問済みにする
            self.map.room(x, y, visit=True)

            # 現在のPrinceの位置座標の更新
            self.prince_location_x = x
            self.prince_location_y = y
            message += 'moved!'
            return message

        # 移動先の部屋は存在するが、ロックされている場合
        elif new_room and new_room.is_locked:
            message = 'Kill the stinker!!!'
            return message

        # 移動先の部屋が存在しない(MAP外に出ようとした)場合
        else:
            message = "Can't go there"
            return message

    def game_data_update(self):
        self.room = self.map.room(self.prince_location_x, self.prince_location_y)
        stinker = 0
        super_stinker = None
        prince = None
        locked_room = None

        for floor_y in self.map.floor:
            for room in floor_y:
                # ロックされた部屋を参照
                if room.is_locked:
                    locked_room = room

                # princeを参照
                if room.prince:
                    prince = room.prince

                # super Stinkerを参照
                if room.stinker and room.stinker.is_super:
                    super_stinker = room.stinker

                # stinkerの参照
                elif room.stinker:
                    # stinkerの体力が0以下ならオブジェクトを削除する
                    if room.stinker.hp <= 0:
                        room.destroy('stinker')

                    # stinkerの残数をカウント
                    else:
                        stinker += 1

        # princeObjがMap上に存在しない or princeのHPが0以下の場合ゲームを終了
        if prince is None or (prince and prince.hp <= 0):
            print('prince is die!!!!!!!!!!!!!')
            input('any key exit')
            exit()

        # superStinkerがMap上に存在しない or superStinkerの体力が0以下の場合ゲームを終了
        if super_stinker is None or (super_stinker and super_stinker.hp <= 0):
            print('prince is save!!!!!!!!!!!!!')
            input('any key exit')
            exit()

        # superStinkerが存在する and ロックされた部屋がある and 通常のstinkerが存在しない場合 superStinkerの部屋を開放
        if super_stinker and locked_room and stinker == 0:
            locked_room.unlock()

        return

    def user_input(self, debug=False):
        message = 'Good luck!'
        while True:
            # ゲームデータの更新
            room = self.map.room(self.prince_location_x, self.prince_location_y)
            self.game_data_update()
            os.system('cls')
            flag_potion = room and room.is_potion and room.prince and (room.prince.hp < room.prince.max_hp)
            flag_attack = room and room.stinker and room.prince

            # 操作ガイドを表示
            self.map.map_print(debug=debug)
            print(message)
            message = ''

            if room and room.prince and room.prince.hp:
                print(f"prince HP:{room.prince.hp}", end=' ')
            if flag_attack:
                print(f"stinker HP:{room.stinker.hp}", end=' ')
            print('')

            print('Move Guide')
            if self.map.get_door_char(self.prince_location_x, self.prince_location_y, diff_y=-1) == 'D':
                print('[W] ↑', end=' ')
            if self.map.get_door_char(self.prince_location_x, self.prince_location_y, diff_x=-1) == 'D':
                print('[A] ←', end=' ')
            if self.map.get_door_char(self.prince_location_x, self.prince_location_y, diff_y=1) == 'D':
                print('[S] ↓', end=' ')
            if self.map.get_door_char(self.prince_location_x, self.prince_location_y, diff_x=1) == 'D':
                print('[D] →', end=' ')
            print('')

            if flag_potion:
                print('[U] Use Potion')
            if flag_attack:
                print('[X] Attack')

            # 入力受付
            user_input = input('INPUT(USER INPUT)\n>')
            if user_input == 'W' or user_input == 'w':
                message = self.move_prince(0, -1)

            elif user_input == 'A' or user_input == 'a':
                message = self.move_prince(-1, 0)

            elif user_input == 'S' or user_input == 's':
                message = self.move_prince(0, 1)

            elif user_input == 'D' or user_input == 'd':
                message = self.move_prince(1, 0)

            elif flag_potion and (user_input == 'U' or user_input == 'u'):
                use_potion = room.prince.use_potion()
                if use_potion:
                    message = 'use potion!'
                    room.destroy('potion')

            elif flag_attack and (user_input == 'X' or user_input == 'x'):
                room.prince.in_damage(room.stinker.attack)
                room.stinker.in_damage(room.prince.attack)

            else:
                continue


    game = Game()
    game.user_input()
