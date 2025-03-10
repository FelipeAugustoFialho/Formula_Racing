from code.Const import WIN_HEIGHT
from code.Enemy import Enemy
from code.Entity import Entity
from code.Menu import Menu
from code.Player import Player
from code.Collision import Collision
from code.Background import Background  # Supondo que você tenha esse módulo
from code.Score import Score


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.top > WIN_HEIGHT:  # Verificando se o inimigo saiu da tela
                print(f"Inimigo {ent} saiu da tela, removendo...")
                ent.health = 0  # Zera a saúde do inimigo

    @staticmethod
    def __verify_collision_entity(ent1, ent2, entity_list, sprite_group):
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            # Colisão entre Player e Enemy
            print(f"Colisão detectada entre {ent1} e {ent2}. Zera a vida do player.")
            ent1.health = 0  # Zera a saúde do Player

            # Adiciona a explosão
            explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
            entity_list.append(explosion)

        elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
            # Colisão entre Enemy e Player
            print(f"Colisão detectada entre {ent1} e {ent2}. Zera a vida do player.")
            ent2.health = 0  # Zera a saúde do Player

            # Adiciona a explosão
            explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
            entity_list.append(explosion)

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity], window):
        if enemy.health <= 0:
            print(f"Inimigo {enemy} derrotado, atualizando o score do jogador.")

            players = [ent for ent in entity_list if isinstance(ent, Player)]  # Garante que só busca Players
            for player in players:
                # Atualiza o score do jogador
                player.score += enemy.score
                print(f"Score do jogador atualizado para {player.score}.")

                # Agora salva o score atualizado
                score = Score(window)  # Passa a janela corretamente para o Score
                score.save(player.score)

                print(f"Score do jogador salvo: {player.score}")

    @staticmethod
    def verify_collision(entity_list: list[Entity], sprite_group):
        for ent1 in entity_list:
            if isinstance(ent1, Collision) or isinstance(ent1, Background):
                continue

            for ent2 in entity_list:
                if isinstance(ent2, Collision) or isinstance(ent2, Background):
                    continue

                if ent1 != ent2 and isinstance(ent1, Player) and isinstance(ent2, Enemy):
                    if ent1.rect.colliderect(ent2.rect):
                        print(f"Colisão detectada entre {ent1} e {ent2}")
                        explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
                        entity_list.append(explosion)
                        ent1.health = 0  # Zera a saúde do player após a colisão

                if isinstance(ent1, Enemy) and isinstance(ent2, Enemy):
                    continue

    @staticmethod
    def verify_health(entity_list: list[Entity],
                      window):  # Adicionei window como argumento para uso do menu, se necessário
        for ent in entity_list:
            if hasattr(ent, 'health'):  # Verifica se a entidade tem 'health'
                if ent.health == 0:
                    if isinstance(ent, Enemy):
                        EntityMediator.__give_score(ent, entity_list, window)
                    entity_list.remove(ent)  # Remove a entidade
                    print(f"Entidade {ent} removida da lista.")
                    if isinstance(ent, Player):  # Se o jogador morrer
                        print(f"Jogador {ent} morreu, indo para o menu!")
                        break  # Interrompe o loop
                        return
                    # menu.run()  # Exibe o menu se necessário

#
#
# #                                    GUARDAR CONFIGURAÇÕES BOAS PARA IMPLEMENTAR
#
# from code.Const import WIN_HEIGHT
# from code.Enemy import Enemy
# from code.Entity import Entity
# from code.Menu import Menu
# from code.Player import Player
# from code.Collision import Collision
# from code.Background import Background  # Supondo que você tenha esse módulo
# from code.Score import Score
#
#
# class EntityMediator:
#
#     @staticmethod
#     def __verify_collision_window(ent: Entity):
#         if isinstance(ent, Enemy):
#             if ent.rect.top > WIN_HEIGHT:  # Verificando se o inimigo saiu da tela
#                 print(f"Inimigo {ent} saiu da tela, removendo...")
#                 ent.health = 0  # Zera a saúde do inimigo
#
#     @staticmethod
#     def __verify_collision_entity(ent1, ent2, entity_list, sprite_group):
#         if isinstance(ent1, Player) and isinstance(ent2, Enemy):
#             # Colisão entre Player e Enemy
#             print(f"Colisão detectada entre {ent1} e {ent2}. Zera a vida do player.")
#             ent1.health = 0  # Zera a saúde do Player
#
#             # Adiciona a explosão
#             explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
#             entity_list.append(explosion)
#
#
#         elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
#             # Colisão entre Enemy e Player
#             print(f"Colisão detectada entre {ent1} e {ent2}. Zera a vida do player.")
#             ent2.health = 0  # Zera a saúde do Player
#
#
#             # Adiciona a explosão
#             explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
#             entity_list.append(explosion)
#
#     @staticmethod
#     def __give_score(enemy: Enemy, entity_list: list[Entity]):
#         if enemy.health <= 0:
#             print(f"Inimigo {enemy} derrotado, atualizando o score do jogador.")
#             players = [ent for ent in entity_list if isinstance(ent, Player)]  # Garante que só busca Players
#             for player in players:
#                 #player.score += enemy.score
#                 player_score = player.score + enemy.score
#
#                 Score(self.window).save(player_score)
#
#                 print(f"Score do jogador atualizado para (ENTITYMEDIATOR){player.score}.")
#
#
#
#     @staticmethod
#     def verify_collision(entity_list: list[Entity], sprite_group):
#         for ent1 in entity_list:
#             if isinstance(ent1, Collision) or isinstance(ent1, Background):
#                 continue
#
#             for ent2 in entity_list:
#                 if isinstance(ent2, Collision) or isinstance(ent2, Background):
#                     continue
#
#                 if ent1 != ent2 and isinstance(ent1, Player) and isinstance(ent2, Enemy):
#                     if ent1.rect.colliderect(ent2.rect):
#                         print(f"Colisão detectada entre {ent1} e {ent2}")
#                         explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
#                         entity_list.append(explosion)
#                         ent1.health = 0  # Zera a saúde do player após a colisão
#
#                 if isinstance(ent1, Enemy) and isinstance(ent2, Enemy):
#                     continue
#
#     @staticmethod
#     def verify_health(entity_list: list[Entity],): #menu: Menu):
#         for ent in entity_list:
#             if hasattr(ent, 'health'):  # Verifica se a entidade tem 'health'
#                 if ent.health == 0:
#                     if isinstance(ent, Enemy):
#                         EntityMediator.__give_score(ent, entity_list)
#                     entity_list.remove(ent)  # Remove a entidade
#                     print(f"Entidade {ent} removida da lista.")
#                     if isinstance(ent, Player):  # Se o jogador morrer
#                         print(f"Jogador {ent} morreu, indo para o menu!")
#                         break  # Interrompe o loop
#                         return
#                        # menu.run()  # Exibe o menu
#
#
#
#
#
#
# # ORIGINAL
#
#
# #
# # from code.Const import WIN_HEIGHT
# # from code.Enemy import Enemy
# # from code.Entity import Entity
# # from code.Menu import Menu
# # from code.Player import Player
# # from code.Collision import Collision
# #
# #
# # class EntityMediator:
# #
# #     @staticmethod
# #     def __verify_collision_window(ent: Entity):
# #         if isinstance(ent, Enemy):  # CONSULTAR ESSE ENEMY
# #             if ent.rect.top > WIN_HEIGHT:  # Verificando se saiu pelo fundo ✅
# #                 ent.health = 0
# #
# #
# #
# #
# #     @staticmethod
# #     def __verify_collision_entity(ent1, ent2, entity_list,sprite_group):
# #         # Verifica se o Player colidiu com um carro inimigo
# #         if isinstance(ent1, Player) and isinstance(ent2, Enemy):
# #             ent1.health = 0  # Zera a vida do Player
# #
# #             # Adiciona a explosão no ponto de colisão
# #             explosion = Collision(ent1.rect.centerx, ent1.rect.centery)
# #             entity_list.append(explosion)
# #
# #         elif isinstance(ent1, Enemy) and isinstance(ent2, Player):
# #             ent2.health = 0  # Zera a vida do Player
# #
# #             # Adiciona a explosão no ponto de colisão
# #
# #             explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
# #             entity_list.append(explosion)
# #
# #
# #
# #     @staticmethod
# #     def __give_score(enemy: Enemy, entity_list: list[Entity]):
# #
# #         if enemy.health <= 0:  # if entity_list.remove():
# #             for ent in entity_list:
# #                 if ent.name == 'Player':
# #                     ent.score += enemy.score
# #
# #     @staticmethod
# #     def verify_collision(entity_list,sprite_group):
# #         for ent1 in entity_list:
# #             for ent2 in entity_list:
# #                 if ent1 != ent2:
# #                     if ent1.rect.colliderect(ent2.rect):
# #                         # Se for uma colisão entre Player e Enemy, criamos a explosão
# #                         if isinstance(ent1, Player) and isinstance(ent2, Enemy):
# #                             explosion = Collision(ent1.rect.centerx, ent1.rect.centery, sprite_group)
# #                             entity_list.append(explosion)
# #
# #
# #
# #     @staticmethod
# #     def verify_health(entity_list):
# #         for ent in entity_list:
# #             if hasattr(ent, 'health'):  # Verifica se a entidade tem o atributo 'health'
# #                 if ent.health == 0:
# #                     entity_list.remove(ent)  # Remove a entidade (por exemplo, se a saúde for zero)
# #
# #
