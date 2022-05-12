bullet_dmg = int(input())
zombie_health = (input().split())
zombie_health = [int(item) for item in zombie_health]
total_bullet_use = 0
zombile_kill_count = []
for i in zombie_health:
    count = i//bullet_dmg
    if i % bullet_dmg != 0:
        count += 1
    zombile_kill_count.append(count+total_bullet_use)
    total_bullet_use += count
print(total_bullet_use)
for item in zombile_kill_count:
    print(item, end=" ")