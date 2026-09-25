---
type: smite-build
god: Neith
mode: Conquest
builds:
- source: community
  aspect: Aspect of Wind
  aspect_pick_rate: 0.3
  aspect_win_rate: 0.59
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.3
    win_rate: 0.52
    alternates:
    - name: Book of Thoth
      pick_rate: 0.21
      win_rate: 0.47
    - name: Tyrfing
      pick_rate: 0.17
      win_rate: 0.47
  - name: The World Stone
    pick_rate: 0.16
    win_rate: 0.57
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.21
      win_rate: 0.37
    - name: Book of Thoth
      pick_rate: 0.14
      win_rate: 0.46
  - name: Rod of Tahuti
    pick_rate: 0.18
    win_rate: 0.63
    alternates:
    - name: The World Stone
      pick_rate: 0.14
      win_rate: 0.25
    - name: Soul Gem
      pick_rate: 0.08
      win_rate: 0.57
  - name: Obsidian Shard
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.24
      win_rate: 0.45
    - name: The Executioner
      pick_rate: 0.07
      win_rate: 0.67
  - name: Dreamer's Idol
    pick_rate: 0.09
    win_rate: 0.71
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.18
      win_rate: 0.38
    - name: Rod of Tahuti
      pick_rate: 0.07
      win_rate: 0.4
  - name: Killing Stone
    pick_rate: 0.09
    win_rate: 0.25
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.09
      win_rate: 0.75
    - name: Dreamer's Idol
      pick_rate: 0.09
      win_rate: 0.5
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.32
    win_rate: 0.59
  - name: Conduit Gem
    pick_rate: 0.18
    win_rate: 0.44
  - name: Hunter's Cowl
    pick_rate: 0.12
    win_rate: 0.64
  source_url: https://smitebrain.com/gods/neith/
  last_verified: '2026-09-25'
  god_win_rate: 0.5333333333333333
  god_matches_won: 48
  god_matches_played: 90
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-25'
  god_matches_analyzed: 2996
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Nimble Ring
  - Soul Gem
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Death Metal, Gluttonous Grimoire,
    Spear of the Magus, Riptalon, Lernaean Bow, The Reaper, Silverbranch Bow, Bragi''s
    Harp, Tekko-Kagi, Hydra''s Lament, Bracer of The Abyss, Heartseeker, Doom Orb,
    Chronos'' Pendant, Deathbringer, Ancient Signet, Blood-Bound Book, Golden Blade,
    Titan''s Bane, Dominance, The Crusher, Demon Blade, Bancroft''s Talon, Toxic Blade,
    Musashi''s Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum Blade,
    Rod of Asclepius, The Cosmic Horror, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.44
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.3
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.4
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.3
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.12
      fit: 0.56
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Nimble Ring
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of the
    Magus, Hydra''s Lament, Bragi''s Harp, Lernaean Bow, Heartseeker, The Reaper,
    Tekko-Kagi, Doom Orb, Ancient Signet, Riptalon, Bracer of The Abyss, Silverbranch
    Bow, Chronos'' Pendant, Dominance, Deathbringer, Bancroft''s Talon, Titan''s Bane,
    Blood-Bound Book, The Crusher, Golden Blade, Transcendence, Arondight, Gem of
    Focus, Musashi''s Dual Swords, Polynomicon, Demon Blade, Runeforged Hammer, Rod
    of Asclepius, Soul Reaver, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.44
    Hydra's Lament:
      total: 0.51
      efficiency: 0.54
      win: 0.57
      pick: 0.0
      fit: 0.42
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.4
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.35
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.39
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.29
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Jotunn's Revenge
  - Death Metal
  - Musashi's Dual Swords
  - Deathbringer
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Deathbringer
  - Musashi's Dual Swords
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
  rationale: 'Crit / auto-attack skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Spear of the Magus, Riptalon, The Reaper, Lernaean Bow, Silverbranch Bow, Bragi''s
    Harp, Tekko-Kagi, Hydra''s Lament, Heartseeker, Bracer of The Abyss, Deathbringer,
    Doom Orb, Chronos'' Pendant, Ancient Signet, Blood-Bound Book, Titan''s Bane,
    The Crusher, Golden Blade, Dominance, Musashi''s Dual Swords, Demon Blade, Bancroft''s
    Talon, Gem of Focus, Toxic Blade, Arondight, Transcendence, Damaru, Rage, Rod
    of Asclepius, Pendulum Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.35
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.51
    Musashi's Dual Swords:
      total: 0.47
      efficiency: 0.46
      win: 0.57
      pick: 0.0
      fit: 0.36
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.36
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.3
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.4
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Death Metal, Gluttonous Grimoire,
    Spear of the Magus, The Reaper, Riptalon, Silverbranch Bow, Tekko-Kagi, Hydra''s
    Lament, Heartseeker, Lernaean Bow, Bragi''s Harp, Doom Orb, Chronos'' Pendant,
    Titan''s Bane, The Crusher, Bracer of The Abyss, Deathbringer, Ancient Signet,
    Blood-Bound Book, Pendulum Blade, Dominance, Golden Blade, Arondight, Gem of Focus,
    Toxic Blade, Bancroft''s Talon, Avatar''s Parashu, Musashi''s Dual Swords, The
    Cosmic Horror, Demon Blade, Transcendence, Runeforged Hammer, Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.33
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.43
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.33
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Rod of Tahuti
  - Obsidian Shard
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Berserker's Shield
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Soul Gem, Berserker''s Shield, Jotunn''s Revenge, Gluttonous
    Grimoire, Rod of Asclepius, Riptalon, The Reaper, Nimble Ring, Shield of the Phoenix,
    Death Metal, Blood-Bound Book, Kinetic Cuirass, Ethereal Staff, Genji''s Guard,
    Breastplate of Valor, Freya''s Tears, Bancroft''s Talon, Spear of the Magus, Runeforged
    Hammer, Yogi''s Necklace, Golden Blade, Lifebinder, Helm of Radiance, Shifter''s
    Shield, Sphere of Negation, Shield Splitter, Lernaean Bow, Pharaoh''s Curse, Chandra''s
    Grace, Phoenix Feather, Hydra''s Lament, Silverbranch Bow, Shogun''s Ofuda, Eye
    of the Storm, Daybreak Gavel, Heartseeker, Erosion.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.57
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.26
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.21
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.31
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.59
    Soul Gem:
      total: 0.57
      efficiency: 0.57
      win: 0.57
      pick: 0.12
      fit: 0.73
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    for this god: Jotunn''s Revenge, Soul Gem, Nimble Ring, Gluttonous Grimoire, Death
    Metal, Spear of the Magus, Riptalon, The Executioner, The Reaper, Silverbranch
    Bow, Tekko-Kagi, Heartseeker, Doom Orb, Lernaean Bow, Titan''s Bane, The Crusher,
    Bragi''s Harp, Hydra''s Lament, Avenging Blade, Bracer of The Abyss, Toxic Blade,
    Chronos'' Pendant, Ancient Signet, Deathbringer, Blood-Bound Book, The Cosmic
    Horror, Pendulum Blade, Avatar''s Parashu, Dominance, Golden Blade, Bancroft''s
    Talon, Gem of Focus, Musashi''s Dual Swords, Arondight, Demon Blade, Oath-Sworn
    Spear.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.45
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.37
    Death Metal:
      total: 0.53
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.42
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.4
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.5
    Dreamer's Idol:
      total: 0.57
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.4
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Riptalon
  - Silverbranch Bow
  - Rod of Tahuti
  - Dreamer's Idol
  flex_slots:
  - Riptalon
  - Silverbranch Bow
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Jotunn''s Revenge, Nimble Ring, Soul Gem, Death Metal, Gluttonous Grimoire,
    Riptalon, Silverbranch Bow, Spear of the Magus, Lernaean Bow, The Reaper, Bragi''s
    Harp, Tekko-Kagi, Bracer of The Abyss, Hydra''s Lament, Golden Blade, Heartseeker,
    Doom Orb, Chronos'' Pendant, Toxic Blade, Ancient Signet, Deathbringer, Dominance,
    Blood-Bound Book, Titan''s Bane, The Crusher, Qin''s Blade, Bancroft''s Talon,
    Gem of Focus, Demon Blade, Musashi''s Dual Swords, Arondight, Transcendence, Rod
    of Asclepius, Runeforged Hammer, Polynomicon.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.3
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.39
    Riptalon:
      total: 0.51
      efficiency: 0.51
      win: 0.57
      pick: 0.0
      fit: 0.52
    Silverbranch Bow:
      total: 0.51
      efficiency: 0.53
      win: 0.57
      pick: 0.0
      fit: 0.46
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.25
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.25
  community_ordered:
  - Rod of Tahuti
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  flex_slots:
  - Dreamer's Idol
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Death Metal, Hydra''s Lament, Gluttonous Grimoire, Chronos'' Pendant, Spear
    of the Magus, Riptalon, Silverbranch Bow, Lernaean Bow, The Reaper, Tekko-Kagi,
    Arondight, Gem of Focus, Heartseeker, Bragi''s Harp, Bracer of The Abyss, Pendulum
    Blade, Doom Orb, Deathbringer, Ancient Signet, Titan''s Bane, The Crusher, Dominance,
    Blood-Bound Book, Golden Blade, Totem of Death, Toxic Blade, Breastplate of Valor,
    Bancroft''s Talon, Musashi''s Dual Swords, Genji''s Guard, Demon Blade, Transcendence,
    Qin''s Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.49
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.52
      pick: 0.3
      fit: 0.49
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.21
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.31
    Dreamer's Idol:
      total: 0.54
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.21
    Soul Gem:
      total: 0.56
      efficiency: 0.57
      win: 0.57
      pick: 0.12
      fit: 0.66
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Nimble Ring
  - Death Metal
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
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
    + win/pick). Underrated for this god: Jotunn''s Revenge, Soul Gem, Nimble Ring,
    Death Metal, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, Riptalon,
    Bracer of The Abyss, The Reaper, Lernaean Bow, Chronos'' Pendant, Silverbranch
    Bow, Hydra''s Lament, Doom Orb, Tekko-Kagi, Ancient Signet, Heartseeker, Blood-Bound
    Book, Gem of Focus, Deathbringer, Bancroft''s Talon, Titan''s Bane, The Crusher,
    Dominance, Golden Blade, Arondight, Rod of Asclepius, The Cosmic Horror, Toxic
    Blade, Polynomicon, Musashi''s Dual Swords, Typhon’s Heart, Demon Blade, Pendulum
    Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.46
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.5
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.35
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.45
    Dreamer's Idol:
      total: 0.56
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.35
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Death Metal
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  flex_slots:
  - Death Metal
  - Nimble Ring
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
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Death Metal, Nimble
    Ring, Soul Gem, Gluttonous Grimoire, Spear of the Magus, Bragi''s Harp, The Reaper,
    Lernaean Bow, Tekko-Kagi, Riptalon, Hydra''s Lament, Heartseeker, Silverbranch
    Bow, Bracer of The Abyss, Doom Orb, Deathbringer, Chronos'' Pendant, Titan''s
    Bane, Ancient Signet, The Crusher, Dominance, Golden Blade, Blood-Bound Book,
    Musashi''s Dual Swords, Bancroft''s Talon, Demon Blade, Arondight, Gem of Focus,
    Transcendence, Toxic Blade, Runeforged Hammer, Pendulum Blade, Avatar''s Parashu,
    Rod of Asclepius.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.39
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.43
    Death Metal:
      total: 0.55
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.53
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.31
    Obsidian Shard:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.3
      fit: 0.41
    Dreamer's Idol:
      total: 0.55
      efficiency: 0.51
      win: 0.71
      pick: 0.19
      fit: 0.31
  community_ordered:
  - Rod of Tahuti
  - Obsidian Shard
  - Dreamer's Idol
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Nimble Ring
  - Spear of Desolation
  - Death Metal
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of Desolation
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Gluttonous Grimoire, Spear of the Magus, Riptalon, Lernaean Bow, The Reaper, Silverbranch
    Bow, Bragi''s Harp, Tekko-Kagi, Hydra''s Lament, Bracer of The Abyss, Heartseeker,
    Doom Orb, Chronos'' Pendant, Deathbringer, Ancient Signet, Blood-Bound Book, Golden
    Blade, Titan''s Bane, Dominance, The Crusher, Demon Blade, Bancroft''s Talon,
    Toxic Blade, Musashi''s Dual Swords, Gem of Focus, Arondight, Transcendence, Pendulum
    Blade, Rod of Asclepius, The Cosmic Horror, Runeforged Hammer.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.57
      pick: 0.0
      fit: 0.36
    Nimble Ring:
      total: 0.55
      efficiency: 0.65
      win: 0.57
      pick: 0.0
      fit: 0.44
    Spear of Desolation:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.3
      fit: 0.38
    Death Metal:
      total: 0.54
      efficiency: 0.61
      win: 0.57
      pick: 0.0
      fit: 0.49
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.63
      pick: 0.28
      fit: 0.3
    Soul Gem:
      total: 0.55
      efficiency: 0.57
      win: 0.57
      pick: 0.12
      fit: 0.56
  community_ordered:
  - Spear of Desolation
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
---
