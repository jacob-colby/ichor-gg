---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.4
  slot_order:
  - name: Transcendence
    pick_rate: 0.28
    win_rate: 0.5
    alternates:
    - name: Tyrfing
      pick_rate: 0.16
      win_rate: 0.57
    - name: Book of Thoth
      pick_rate: 0.16
      win_rate: 0.29
  - name: Odysseus' Bow
    pick_rate: 0.11
    win_rate: 0.43
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.09
      win_rate: 0.5
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.42
  - name: Polynomicon
    pick_rate: 0.11
    win_rate: 0.31
    alternates:
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.5
    - name: Hydra's Lament
      pick_rate: 0.07
      win_rate: 0.67
  - name: Rod of Tahuti
    pick_rate: 0.13
    win_rate: 0.67
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.33
    - name: Pendulum Blade
      pick_rate: 0.07
      win_rate: 0.5
  - name: Obsidian Shard
    pick_rate: 0.1
    win_rate: 0.64
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.13
      win_rate: 0.21
    - name: Riptalon
      pick_rate: 0.06
      win_rate: 0.33
  - name: Void Shard
    pick_rate: 0.07
    win_rate: 0.17
    alternates:
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.4
    - name: Bow
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.14
    win_rate: 0.44
  - name: Conduit Gem
    pick_rate: 0.11
    win_rate: 0.43
  - name: Sharpshooter's Arrow
    pick_rate: 0.11
    win_rate: 0.57
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-08-30'
  god_win_rate: 0.4453125
  god_matches_won: 57
  god_matches_played: 128
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-30'
  god_matches_analyzed: 5563
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Tekko-Kagi, The Reaper, Gluttonous Grimoire, Heartseeker, Bragi''s
    Harp, Spear of the Magus, Deathbringer, Golden Blade, Spear of Desolation, Dominance,
    Demon Blade, The Crusher, Bracer of The Abyss, Musashi''s Dual Swords, Pendulum
    Blade, Toxic Blade, Doom Orb, Damaru, Rage, The World Stone, Blood-Bound Book,
    Ancient Signet, Runeforged Hammer, Arondight, Avatar''s Parashu, Dreamer''s Idol,
    Riptalon, Qin''s Blade, Chronos'' Pendant, Bancroft''s Talon, Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.37
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.18
    Tyrfing:
      total: 0.52
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.58
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.32
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.2
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.3
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Tyrfing
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Hydra''s
    Lament, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Spear of Desolation, Spear of the Magus, Bragi''s Harp, Lernaean Bow, Heartseeker,
    The Reaper, Tekko-Kagi, Doom Orb, Ancient Signet, The World Stone, Bracer of The
    Abyss, Chronos'' Pendant, Dominance, Deathbringer, Pendulum Blade, Bancroft''s
    Talon, Blood-Bound Book, The Crusher, Dreamer''s Idol, Golden Blade, Arondight,
    Gem of Focus, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Rod of Asclepius,
    Soul Reaver, Riptalon, Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.44
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.48
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.42
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.35
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.39
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Hydra's Lament
  - Death Metal
  - Demon Blade
  - Deathbringer
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Deathbringer
  - Demon Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem,
    Gluttonous Grimoire, Lernaean Bow, The Reaper, Tekko-Kagi, Deathbringer, Spear
    of the Magus, Heartseeker, Spear of Desolation, Bragi''s Harp, Demon Blade, Golden
    Blade, Dominance, Musashi''s Dual Swords, The Crusher, Bracer of The Abyss, Pendulum
    Blade, Toxic Blade, Doom Orb, Damaru, Rage, The World Stone, Blood-Bound Book,
    Ancient Signet, Dreamer''s Idol, Chronos'' Pendant, Riptalon, Avatar''s Parashu,
    Runeforged Hammer, Arondight, Qin''s Blade, Bancroft''s Talon, Silverbranch Bow.'
  slot_scores:
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.29
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.49
    Demon Blade:
      total: 0.44
      efficiency: 0.38
      win: 0.46
      pick: 0.0
      fit: 0.67
    Deathbringer:
      total: 0.45
      efficiency: 0.51
      win: 0.46
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.2
    Obsidian Shard:
      total: 0.54
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Hydra''s Lament, Jotunn''s Revenge, Soul Gem, Nimble Ring, Death Metal, Gluttonous
    Grimoire, Spear of Desolation, Spear of the Magus, The Reaper, Tekko-Kagi, Heartseeker,
    Lernaean Bow, Pendulum Blade, Bragi''s Harp, Doom Orb, Chronos'' Pendant, The
    World Stone, The Crusher, Bracer of The Abyss, Dreamer''s Idol, Deathbringer,
    Ancient Signet, Blood-Bound Book, Dominance, Golden Blade, Arondight, Gem of Focus,
    Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s Dual Swords, The
    Cosmic Horror, Demon Blade, Runeforged Hammer, Rod of Asclepius, Riptalon, Silverbranch
    Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.46
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.13
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.36
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.37
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.33
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Amanita Charm, Jotunn''s Revenge, Berserker''s Shield,
    Soul Gem, The Reaper, Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius,
    Nimble Ring, Death Metal, Kinetic Cuirass, Runeforged Hammer, Golden Blade, Freya''s
    Tears, Genji''s Guard, Blood-Bound Book, Breastplate of Valor, Ethereal Staff,
    Yogi''s Necklace, Shifter''s Shield, Shield Splitter, Bancroft''s Talon, Lernaean
    Bow, Pharaoh''s Curse, Eye of the Storm, Shogun''s Ofuda, Phoenix Feather, Spear
    of the Magus, Lifebinder, Tekko-Kagi, Erosion, Helm of Radiance, Heartseeker,
    Eye of Providence, Daybreak Gavel, Toxic Blade, Chandra''s Grace, Riptalon, Silverbranch
    Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.25
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.12
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.24
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.14
    Obsidian Shard:
      total: 0.52
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.24
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Tyrfing
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Jotunn''s Revenge, Hydra''s Lament, Soul Gem, Nimble Ring, Gluttonous
    Grimoire, Death Metal, The Reaper, Tekko-Kagi, Spear of the Magus, Heartseeker,
    Spear of Desolation, Lernaean Bow, The Crusher, Pendulum Blade, Doom Orb, Avenging
    Blade, Toxic Blade, The Executioner, The World Stone, Dreamer''s Idol, Bragi''s
    Harp, Deathbringer, Avatar''s Parashu, Dominance, Golden Blade, Bracer of The
    Abyss, Riptalon, Demon Blade, Musashi''s Dual Swords, Silverbranch Bow, The Cosmic
    Horror, Oath-Sworn Spear, Ancient Signet, Blood-Bound Book, Runeforged Hammer,
    Chronos'' Pendant, Arondight.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.48
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.15
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.5
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.28
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.35
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.45
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Lernaean Bow
  - Tyrfing
  - Hydra's Lament
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Hydra''s Lament, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear
    of the Magus, Bragi''s Harp, Heartseeker, Spear of Desolation, Toxic Blade, Deathbringer,
    Dominance, Bracer of The Abyss, Qin''s Blade, Demon Blade, The Crusher, Riptalon,
    Musashi''s Dual Swords, Doom Orb, Ancient Signet, Silverbranch Bow, The World
    Stone, Blood-Bound Book, Chronos'' Pendant, Dreamer''s Idol, Sun Beam Bow, Runeforged
    Hammer, Arondight, Damaru, Bancroft''s Talon, Rage, Berserker''s Shield.'
  slot_scores:
    Lernaean Bow:
      total: 0.46
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.46
    Tyrfing:
      total: 0.53
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.62
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.25
    Nimble Ring:
      total: 0.49
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.17
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Tyrfing
  - Hydra's Lament
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Tyrfing
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge,
    Soul Gem, Nimble Ring, Spear of Desolation, Death Metal, Gluttonous Grimoire,
    Chronos'' Pendant, Pendulum Blade, Spear of the Magus, Lernaean Bow, The Reaper,
    Arondight, Gem of Focus, Tekko-Kagi, Bragi''s Harp, Heartseeker, Bracer of The
    Abyss, Deathbringer, Doom Orb, Ancient Signet, Dominance, Blood-Bound Book, The
    World Stone, Golden Blade, Totem of Death, The Crusher, Dreamer''s Idol, Breastplate
    of Valor, Toxic Blade, Bancroft''s Talon, Musashi''s Dual Swords, Demon Blade,
    Genji''s Guard, Qin''s Blade, Riptalon, Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.48
    Tyrfing:
      total: 0.5
      efficiency: 0.48
      win: 0.57
      pick: 0.16
      fit: 0.41
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.47
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.2
    Obsidian Shard:
      total: 0.53
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.3
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Intelligence build — this kit scales on it (efficiency + fit
    + win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge, Nimble
    Ring, Soul Gem, Death Metal, Gluttonous Grimoire, Spear of Desolation, Spear of
    the Magus, Bragi''s Harp, Lernaean Bow, The Reaper, Bracer of The Abyss, Chronos''
    Pendant, Tekko-Kagi, Doom Orb, Heartseeker, The World Stone, Ancient Signet, Blood-Bound
    Book, Dreamer''s Idol, Pendulum Blade, Deathbringer, Gem of Focus, Bancroft''s
    Talon, The Crusher, Dominance, Golden Blade, Arondight, Rod of Asclepius, Musashi''s
    Dual Swords, The Cosmic Horror, Demon Blade, Toxic Blade, Typhon’s Heart, Riptalon,
    Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.38
    Transcendence:
      total: 0.44
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.13
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.34
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.34
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Nimble Ring
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Hydra''s Lament, Jotunn''s Revenge,
    Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Spear
    of Desolation, Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi, Heartseeker,
    Bracer of The Abyss, Doom Orb, Deathbringer, The World Stone, The Crusher, Ancient
    Signet, Dominance, Golden Blade, Dreamer''s Idol, Blood-Bound Book, Chronos''
    Pendant, Demon Blade, Musashi''s Dual Swords, Bancroft''s Talon, Toxic Blade,
    Runeforged Hammer, Avatar''s Parashu, Arondight, Gem of Focus, The Cosmic Horror,
    Rod of Asclepius, Riptalon, Silverbranch Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.36
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.5
      pick: 0.28
      fit: 0.18
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.67
      pick: 0.11
      fit: 0.31
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.45
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.33
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.64
      pick: 0.22
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Lernaean Bow
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Lernaean Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Riptalon, Lernaean Bow, Tekko-Kagi, The Reaper, Gluttonous Grimoire, Silverbranch
    Bow, Heartseeker, Bragi''s Harp, Spear of the Magus, Deathbringer, Hydra''s Lament,
    Golden Blade, Spear of Desolation, Dominance, Demon Blade, The Crusher, Bracer
    of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, The
    World Stone, Blood-Bound Book, Ancient Signet, Runeforged Hammer, Arondight, Avatar''s
    Parashu, Dreamer''s Idol, Qin''s Blade, Chronos'' Pendant, Pendulum Blade, Bancroft''s
    Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.47
      efficiency: 0.52
      win: 0.46
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.12
      fit: 0.37
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.46
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.49
      efficiency: 0.61
      win: 0.46
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.67
      pick: 0.22
      fit: 0.2
    Soul Gem:
      total: 0.47
      efficiency: 0.57
      win: 0.46
      pick: 0.0
      fit: 0.43
  starter: *id001
---
