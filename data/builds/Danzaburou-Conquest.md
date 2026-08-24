---
type: smite-build
god: Danzaburou
mode: Conquest
builds:
- source: community
  aspect: Aspect of Fellowship
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.64
  slot_order:
  - name: Transcendence
    pick_rate: 0.29
    win_rate: 0.64
    alternates:
    - name: Tyrfing
      pick_rate: 0.1
      win_rate: 0.38
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.56
  - name: Jotunn's Revenge
    pick_rate: 0.15
    win_rate: 0.65
    alternates:
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.49
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.72
  - name: The World Stone
    pick_rate: 0.13
    win_rate: 0.74
    alternates:
    - name: Polynomicon
      pick_rate: 0.06
      win_rate: 0.59
    - name: Silverbranch Bow
      pick_rate: 0.06
      win_rate: 0.42
  - name: Rod of Tahuti
    pick_rate: 0.1
    win_rate: 0.63
    alternates:
    - name: Silverbranch Bow
      pick_rate: 0.08
      win_rate: 0.56
    - name: The Executioner
      pick_rate: 0.08
      win_rate: 0.45
  - name: Silverbranch Bow
    pick_rate: 0.06
    win_rate: 0.68
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.54
    - name: Riptalon
      pick_rate: 0.05
      win_rate: 0.68
  - name: Titan's Bane
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.79
    - name: Manchu Bow
      pick_rate: 0.05
      win_rate: 0.46
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.16
    win_rate: 0.6
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.49
  - name: Sharpshooter's Arrow
    pick_rate: 0.1
    win_rate: 0.52
  source_url: https://smitebrain.com/gods/danzaburou/
  last_verified: '2026-08-24'
  god_win_rate: 0.5586206896551724
  god_matches_won: 243
  god_matches_played: 435
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-24'
  god_matches_analyzed: 17273
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Silverbranch Bow
  - The World Stone
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
    this god: Riptalon, Nimble Ring, Death Metal, Silverbranch Bow, Soul Gem, Lernaean
    Bow, Tekko-Kagi, The Reaper, Gluttonous Grimoire, Heartseeker, Bragi''s Harp,
    Spear of the Magus, Deathbringer, Hydra''s Lament, Golden Blade, Spear of Desolation,
    Obsidian Shard, Dominance, Demon Blade, The Crusher, Bracer of The Abyss, Musashi''s
    Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, Blood-Bound Book, Ancient Signet,
    Runeforged Hammer, Arondight, Avatar''s Parashu, Dreamer''s Idol, Qin''s Blade,
    Chronos'' Pendant, Pendulum Blade, Bancroft''s Talon, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.37
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.48
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.68
      pick: 0.11
      fit: 0.55
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.68
      pick: 0.13
      fit: 0.45
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.74
      pick: 0.2
      fit: 0.2
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.2
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Death Metal
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Death
    Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Riptalon, Book of Thoth, Silverbranch
    Bow, Spear of Desolation, Spear of the Magus, Hydra''s Lament, Obsidian Shard,
    Bragi''s Harp, Lernaean Bow, Heartseeker, The Reaper, Tekko-Kagi, Doom Orb, Ancient
    Signet, Bracer of The Abyss, Chronos'' Pendant, Dominance, Deathbringer, Bancroft''s
    Talon, Blood-Bound Book, The Crusher, Dreamer''s Idol, Golden Blade, Arondight,
    Gem of Focus, Musashi''s Dual Swords, Demon Blade, Runeforged Hammer, Rod of Asclepius,
    Soul Reaver, Pendulum Blade, Polynomicon, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.24
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.44
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.64
      pick: 0.29
      fit: 0.24
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.51
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.74
      pick: 0.2
      fit: 0.35
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - Demon Blade
  - Deathbringer
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
    this god: Death Metal, Riptalon, Nimble Ring, Silverbranch Bow, Soul Gem, Gluttonous
    Grimoire, Lernaean Bow, The Reaper, Tekko-Kagi, Deathbringer, Spear of the Magus,
    Heartseeker, Spear of Desolation, Obsidian Shard, Bragi''s Harp, Demon Blade,
    Hydra''s Lament, Golden Blade, Dominance, Musashi''s Dual Swords, The Crusher,
    Bracer of The Abyss, Toxic Blade, Doom Orb, Damaru, Rage, Blood-Bound Book, Ancient
    Signet, Dreamer''s Idol, Chronos'' Pendant, Avatar''s Parashu, Runeforged Hammer,
    Arondight, Qin''s Blade, Bancroft''s Talon, Pendulum Blade, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.34
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.49
    Riptalon:
      total: 0.57
      efficiency: 0.51
      win: 0.68
      pick: 0.11
      fit: 0.54
    Silverbranch Bow:
      total: 0.56
      efficiency: 0.53
      win: 0.68
      pick: 0.13
      fit: 0.44
    Demon Blade:
      total: 0.52
      efficiency: 0.38
      win: 0.63
      pick: 0.0
      fit: 0.67
    Deathbringer:
      total: 0.53
      efficiency: 0.51
      win: 0.63
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
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
    god: Soul Gem, Nimble Ring, Death Metal, Riptalon, Silverbranch Bow, Gluttonous
    Grimoire, Spear of Desolation, Spear of the Magus, Obsidian Shard, The Reaper,
    Tekko-Kagi, Hydra''s Lament, Heartseeker, Lernaean Bow, Bragi''s Harp, Doom Orb,
    Chronos'' Pendant, The Crusher, Bracer of The Abyss, Dreamer''s Idol, Deathbringer,
    Ancient Signet, Blood-Bound Book, Pendulum Blade, Dominance, Golden Blade, Arondight,
    Gem of Focus, Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s Dual
    Swords, The Cosmic Horror, Demon Blade, Runeforged Hammer, Rod of Asclepius, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.53
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.13
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.46
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.64
      pick: 0.29
      fit: 0.13
    The World Stone:
      total: 0.57
      efficiency: 0.52
      win: 0.74
      pick: 0.2
      fit: 0.33
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.33
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Death Metal
  - Riptalon
  - Amanita Charm
  flex_slots:
  - Death Metal
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Riptalon, Berserker''s Shield, Soul Gem, The Reaper,
    Gluttonous Grimoire, Shield of the Phoenix, Rod of Asclepius, Nimble Ring, Death
    Metal, Kinetic Cuirass, Silverbranch Bow, Runeforged Hammer, Golden Blade, Freya''s
    Tears, Genji''s Guard, Blood-Bound Book, Breastplate of Valor, Ethereal Staff,
    Yogi''s Necklace, Shifter''s Shield, Shield Splitter, Bancroft''s Talon, Lernaean
    Bow, Pharaoh''s Curse, Eye of the Storm, Shogun''s Ofuda, Phoenix Feather, Spear
    of the Magus, Lifebinder, Tekko-Kagi, Erosion, Helm of Radiance, Heartseeker,
    Hydra''s Lament, Eye of Providence, Daybreak Gavel, Toxic Blade, Chandra''s Grace,
    Tyrfing.'
  slot_scores:
    Berserker's Shield:
      total: 0.58
      efficiency: 0.68
      win: 0.63
      pick: 0.0
      fit: 0.39
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.25
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.63
      pick: 0.0
      fit: 0.43
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.32
    Riptalon:
      total: 0.59
      efficiency: 0.51
      win: 0.68
      pick: 0.11
      fit: 0.67
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.63
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
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
    for this god: Riptalon, Silverbranch Bow, Soul Gem, Nimble Ring, Gluttonous Grimoire,
    Death Metal, The Reaper, Tekko-Kagi, Spear of the Magus, Heartseeker, Obsidian
    Shard, Spear of Desolation, Lernaean Bow, The Crusher, Doom Orb, Avenging Blade,
    Toxic Blade, Hydra''s Lament, Dreamer''s Idol, Bragi''s Harp, Deathbringer, Avatar''s
    Parashu, Dominance, Golden Blade, Pendulum Blade, Bracer of The Abyss, Demon Blade,
    Musashi''s Dual Swords, The Cosmic Horror, Oath-Sworn Spear, Ancient Signet, Blood-Bound
    Book, Runeforged Hammer, Chronos'' Pendant, Arondight, The Executioner, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.04
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.48
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.64
      pick: 0.29
      fit: 0.15
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.68
      pick: 0.11
      fit: 0.63
    Silverbranch Bow:
      total: 0.58
      efficiency: 0.53
      win: 0.68
      pick: 0.13
      fit: 0.55
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Riptalon
  - Silverbranch Bow
  - The World Stone
  flex_slots:
  - Death Metal
  - The World Stone
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
    this god: Riptalon, Silverbranch Bow, Nimble Ring, Death Metal, Soul Gem, Lernaean
    Bow, Gluttonous Grimoire, Tekko-Kagi, Golden Blade, The Reaper, Spear of the Magus,
    Bragi''s Harp, Heartseeker, Obsidian Shard, Spear of Desolation, Toxic Blade,
    Hydra''s Lament, Deathbringer, Dominance, Bracer of The Abyss, Qin''s Blade, Demon
    Blade, The Crusher, Musashi''s Dual Swords, Doom Orb, Ancient Signet, Blood-Bound
    Book, Chronos'' Pendant, Dreamer''s Idol, Sun Beam Bow, Runeforged Hammer, Arondight,
    Damaru, Bancroft''s Talon, Rage, Berserker''s Shield, Tyrfing.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.28
    Nimble Ring:
      total: 0.56
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.36
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.37
    Riptalon:
      total: 0.58
      efficiency: 0.51
      win: 0.68
      pick: 0.11
      fit: 0.6
    Silverbranch Bow:
      total: 0.57
      efficiency: 0.53
      win: 0.68
      pick: 0.13
      fit: 0.52
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.74
      pick: 0.2
      fit: 0.17
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Book of Thoth
  - Transcendence
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
    + fit + win/pick). Underrated for this god: Soul Gem, Nimble Ring, Spear of Desolation,
    Riptalon, Death Metal, Silverbranch Bow, Hydra''s Lament, Gluttonous Grimoire,
    Chronos'' Pendant, Spear of the Magus, Lernaean Bow, Obsidian Shard, The Reaper,
    Arondight, Gem of Focus, Tekko-Kagi, Bragi''s Harp, Heartseeker, Bracer of The
    Abyss, Pendulum Blade, Deathbringer, Doom Orb, Ancient Signet, Dominance, Blood-Bound
    Book, Golden Blade, Totem of Death, The Crusher, Dreamer''s Idol, Breastplate
    of Valor, Toxic Blade, Bancroft''s Talon, Musashi''s Dual Swords, Demon Blade,
    Genji''s Guard, Qin''s Blade, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.08
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.48
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.64
      pick: 0.29
      fit: 0.08
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.58
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.65
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - The World Stone
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
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
    + win/pick). Underrated for this god: Nimble Ring, Soul Gem, Death Metal, Gluttonous
    Grimoire, Riptalon, Spear of Desolation, Silverbranch Bow, Spear of the Magus,
    Obsidian Shard, Book of Thoth, Bragi''s Harp, Lernaean Bow, The Reaper, Hydra''s
    Lament, Bracer of The Abyss, Chronos'' Pendant, Tekko-Kagi, Doom Orb, Heartseeker,
    Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Deathbringer, Gem of Focus,
    Bancroft''s Talon, The Crusher, Dominance, Golden Blade, Arondight, Rod of Asclepius,
    Musashi''s Dual Swords, The Cosmic Horror, Demon Blade, Toxic Blade, Pendulum
    Blade, Typhon’s Heart, Polynomicon, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.2
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.38
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.64
      pick: 0.29
      fit: 0.13
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.45
    The World Stone:
      total: 0.58
      efficiency: 0.52
      win: 0.74
      pick: 0.2
      fit: 0.34
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  flex_slots:
  - Book of Thoth
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
    + fit + win/pick). Underrated for this god: Death Metal, Nimble Ring, Soul Gem,
    Riptalon, Gluttonous Grimoire, Silverbranch Bow, Spear of the Magus, Obsidian
    Shard, Spear of Desolation, Bragi''s Harp, The Reaper, Book of Thoth, Lernaean
    Bow, Tekko-Kagi, Heartseeker, Bracer of The Abyss, Hydra''s Lament, Doom Orb,
    Deathbringer, The Crusher, Ancient Signet, Dominance, Golden Blade, Dreamer''s
    Idol, Blood-Bound Book, Chronos'' Pendant, Demon Blade, Musashi''s Dual Swords,
    Bancroft''s Talon, Toxic Blade, Runeforged Hammer, Avatar''s Parashu, Arondight,
    Gem of Focus, The Cosmic Horror, Rod of Asclepius, Tyrfing.'
  slot_scores:
    Book of Thoth:
      total: 0.54
      efficiency: 0.51
      win: 0.72
      pick: 0.14
      fit: 0.18
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.36
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.64
      pick: 0.29
      fit: 0.18
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.45
    Death Metal:
      total: 0.58
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.55
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.33
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
    Underrated for this god: Nimble Ring, Death Metal, Soul Gem, Riptalon, Lernaean
    Bow, Tekko-Kagi, Tyrfing, The Reaper, Gluttonous Grimoire, Silverbranch Bow, Heartseeker,
    Bragi''s Harp, Spear of the Magus, Deathbringer, Hydra''s Lament, Golden Blade,
    Spear of Desolation, Obsidian Shard, Dominance, Demon Blade, The Crusher, Bracer
    of The Abyss, Musashi''s Dual Swords, Toxic Blade, Doom Orb, Damaru, Rage, Blood-Bound
    Book, Ancient Signet, Runeforged Hammer, Arondight, Avatar''s Parashu, Dreamer''s
    Idol, Qin''s Blade, Chronos'' Pendant, Pendulum Blade, Bancroft''s Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.54
      efficiency: 0.52
      win: 0.63
      pick: 0.0
      fit: 0.53
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.37
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.48
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.43
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - The World Stone
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - The World Stone
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
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Nimble Ring, Death Metal, Soul Gem,
    Riptalon, Lernaean Bow, Tekko-Kagi, Tyrfing, The Reaper, Gluttonous Grimoire,
    Silverbranch Bow, Heartseeker, Bragi''s Harp, Spear of the Magus, Deathbringer,
    Hydra''s Lament, Golden Blade, Spear of Desolation, Obsidian Shard, Dominance,
    Demon Blade, The Crusher, Bracer of The Abyss, Musashi''s Dual Swords, Toxic Blade,
    Doom Orb, Damaru, Rage, Blood-Bound Book, Ancient Signet, Runeforged Hammer, Arondight,
    Avatar''s Parashu, Dreamer''s Idol, Qin''s Blade, Chronos'' Pendant, Pendulum
    Blade, Bancroft''s Talon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.2
      fit: 0.37
    Nimble Ring:
      total: 0.57
      efficiency: 0.65
      win: 0.63
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.57
      efficiency: 0.61
      win: 0.63
      pick: 0.0
      fit: 0.48
    The World Stone:
      total: 0.55
      efficiency: 0.52
      win: 0.74
      pick: 0.2
      fit: 0.2
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.63
      pick: 0.17
      fit: 0.2
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.63
      pick: 0.0
      fit: 0.43
  swaps:
  - added: The World Stone
    removed: Lernaean Bow
    reason: community 74% win over 57 matches (vs 56% on this god), taking the model's
      weakest slot from Lernaean Bow
  starter: *id001
---
