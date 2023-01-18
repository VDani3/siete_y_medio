/*INFORMES*/

/* 1 */



/* 2 */

select cardgame_id "Identificador de partida", player_id "Identificador de jugador", max(bet_points) "Apuesta mas alta"
from player_game_round
group by 1, 2;

/* 3 */

select cardgame_id "Identificador de partida", player_id "Identificador de jugador", min(bet_points) "Apuesta mas baja"
from player_game_round
where is_bank = 0 
group by 1, 2;

/* 4 */



/* 5 */

select cardgame_id "Identificador de partida", max(ending_round_points-starting_round_points) "Puntos ganados"
from player_game_round
where player_id = (select player_id from player where human = 0)
group by 1;

/* 6 */



/* 7 */

select cardgame_id "Identificador de partida", count(distinct player_id) "Cantidad usuarios banca"
from player_game_round
where is_bank = 1
group by 1;

/* 8 */

select cardgame_id "Identificador de partida", avg(bet_points) "Apuesta media"
from player_game_round
where bet_points >= (select avg(bet_points) from player_game_round)
group by 1;

/* 9 */

select cardgame_id "Identificador de partida", avg(bet_points) "Apuesta media (1ª ronda)"
from player_game_round
where bet_points >= (select avg(bet_points) from player_game_round) and round_num = 1;

/* 10 */

select cardgame_id "Identificador de partida", avg(bet_points) "Apuesta media (ultima ronda)"
from player_game_round
where bet_points >= (select avg(bet_points) from player_game_round) and round_num = max(round_num);
