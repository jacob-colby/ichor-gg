---
type: smite-build
god: Medusa
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.71
    win_rate: 0.47
    alternates:
    - name: Transcendence
      pick_rate: 0.14
      win_rate: 0.33
    - name: Avenging Blade
      pick_rate: 0.05
      win_rate: 1.0
  - name: Dagger of Frenzy
    pick_rate: 0.33
    win_rate: 0.43
    alternates:
    - name: Tyrfing
      pick_rate: 0.29
      win_rate: 0.5
    - name: Barbed Carver
      pick_rate: 0.1
      win_rate: 0.5
  - name: Dominance
    pick_rate: 0.2
    win_rate: 0.75
    alternates:
    - name: The Executioner
      pick_rate: 0.2
      win_rate: 0.25
    - name: Odysseus' Bow
      pick_rate: 0.1
      win_rate: 0.5
  - name: Riptalon
    pick_rate: 0.3
    win_rate: 0.33
    alternates:
    - name: The Executioner
      pick_rate: 0.2
      win_rate: 0.75
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.5
  - name: Deathbringer
    pick_rate: 0.22
    win_rate: 0.5
    alternates:
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.67
    - name: Titan's Bane
      pick_rate: 0.17
      win_rate: 0.33
  - name: Skeggox
    pick_rate: 0.17
    win_rate: 1.0
    alternates:
    - name: Riptalon
      pick_rate: 0.17
      win_rate: 0.5
    - name: Musashi's Dual Swords
      pick_rate: 0.08
      win_rate: 1.0
  community_starters:
  - name: Sharpshooter's Arrow
    pick_rate: 0.24
    win_rate: 0.8
  - name: Gilded Arrow
    pick_rate: 0.19
    win_rate: 0.0
  - name: Bluestone Brooch
    pick_rate: 0.14
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/medusa/
  last_verified: '2026-10-21'
  god_win_rate: 0.47619047619047616
  god_matches_won: 10
  god_matches_played: 21
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: core
  slot_order:
  - Avenging Blade
  - The Executioner
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Musashi's Dual Swords
  flex_slots:
  - The Executioner
  - Death Metal
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Lernaean Bow, Gluttonous Grimoire, Silverbranch Bow, Tekko-Kagi, The Reaper, Spear
    of Desolation, Hydra''s Lament, Spear of the Magus, Bragi''s Harp, Obsidian Shard,
    Golden Blade, Demon Blade, Bracer of The Abyss, The Crusher, Toxic Blade, Doom
    Orb, Chronos'' Pendant, Arondight, The World Stone, Ancient Signet, Blood-Bound
    Book, Qin''s Blade, Pendulum Blade, Dreamer''s Idol, Damaru, Rage, Runeforged
    Hammer, Avatar''s Parashu, Bancroft''s Talon, Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.25
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.75
      pick: 0.33
      fit: 0.34
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.43
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.49
    Musashi's Dual Swords:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.39
  community_ordered:
  - Avenging Blade
  - The Executioner
  - Dominance
  - Musashi's Dual Swords
  starter: &id001
    base: Gilded Arrow
    upgrade: Sharpshooter's Arrow
- source: suggested
  archetype: mana-stack
  slot_order:
  - Avenging Blade
  - The Executioner
  - Jotunn's Revenge
  - Dominance
  - Musashi's Dual Swords
  - Rod of Tahuti
  flex_slots:
  - Jotunn's Revenge
  - The Executioner
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Rod
    of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire,
    Spear of Desolation, Spear of the Magus, Hydra''s Lament, Obsidian Shard, Bragi''s
    Harp, Lernaean Bow, The Reaper, Tekko-Kagi, Doom Orb, Ancient Signet, The World
    Stone, Bracer of The Abyss, Silverbranch Bow, Chronos'' Pendant, Bancroft''s Talon,
    Blood-Bound Book, The Crusher, Golden Blade, Dreamer''s Idol, Arondight, Gem of
    Focus, Book of Thoth, Polynomicon, Demon Blade, Runeforged Hammer, Rod of Asclepius,
    Soul Reaver, Pendulum Blade, Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.28
    The Executioner:
      total: 0.52
      efficiency: 0.35
      win: 0.75
      pick: 0.33
      fit: 0.26
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.44
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.5
    Musashi's Dual Swords:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.34
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Avenging Blade
  - The Executioner
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
- source: suggested
  archetype: crit
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  flex_slots:
  - Death Metal
  - Deathbringer
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
    this god: Rod of Tahuti, Jotunn''s Revenge, Death Metal, Nimble Ring, Soul Gem,
    Gluttonous Grimoire, Lernaean Bow, Silverbranch Bow, The Reaper, Tekko-Kagi, Spear
    of Desolation, Hydra''s Lament, Spear of the Magus, Obsidian Shard, Bragi''s Harp,
    Golden Blade, Demon Blade, The Crusher, Bracer of The Abyss, Toxic Blade, Doom
    Orb, Chronos'' Pendant, Arondight, Damaru, The World Stone, Rage, Ancient Signet,
    Blood-Bound Book, Dreamer''s Idol, Pendulum Blade, Qin''s Blade, Runeforged Hammer,
    Avatar''s Parashu, Bancroft''s Talon, Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.24
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.38
    Death Metal:
      total: 0.51
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.46
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.46
    Musashi's Dual Swords:
      total: 0.69
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.41
    Deathbringer:
      total: 0.49
      efficiency: 0.51
      win: 0.5
      pick: 0.48
      fit: 0.41
  community_ordered:
  - Avenging Blade
  - Dominance
  - Musashi's Dual Swords
  - Deathbringer
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Avenging Blade
  - The Executioner
  - Jotunn's Revenge
  - Dominance
  - Musashi's Dual Swords
  - Soul Gem
  flex_slots:
  - The Executioner
  - Soul Gem
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
    god: Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Nimble Ring, Death Metal, Gluttonous
    Grimoire, Spear of Desolation, Spear of the Magus, Obsidian Shard, The Reaper,
    Silverbranch Bow, Tekko-Kagi, Hydra''s Lament, Lernaean Bow, Bragi''s Harp, Doom
    Orb, Chronos'' Pendant, The World Stone, The Crusher, Bracer of The Abyss, Dreamer''s
    Idol, Ancient Signet, Blood-Bound Book, Golden Blade, Pendulum Blade, Toxic Blade,
    Arondight, Gem of Focus, Bancroft''s Talon, Avatar''s Parashu, The Cosmic Horror,
    Demon Blade, Runeforged Hammer, Rod of Asclepius, Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.23
    The Executioner:
      total: 0.52
      efficiency: 0.35
      win: 0.75
      pick: 0.33
      fit: 0.27
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.46
    Dominance:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.4
    Musashi's Dual Swords:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.3
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Avenging Blade
  - The Executioner
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Avenging Blade
  - Berserker's Shield
  - Dominance
  - Musashi's Dual Swords
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Rod of Tahuti, Soul Gem, Berserker''s Shield, Jotunn''s
    Revenge, The Reaper, Shield of the Phoenix, Gluttonous Grimoire, Rod of Asclepius,
    Nimble Ring, Kinetic Cuirass, Death Metal, Genji''s Guard, Freya''s Tears, Breastplate
    of Valor, Golden Blade, Blood-Bound Book, Runeforged Hammer, Ethereal Staff, Yogi''s
    Necklace, Shifter''s Shield, Bancroft''s Talon, Shield Splitter, Pharaoh''s Curse,
    Lernaean Bow, Chandra''s Grace, Phoenix Feather, Shogun''s Ofuda, Spear of the
    Magus, Hydra''s Lament, Spear of Desolation, Silverbranch Bow, Eye of the Storm,
    Lifebinder, Helm of Radiance, Erosion, Toxic Blade, Daybreak Gavel, Eye of Providence,
    Obsidian Shard.'
  slot_scores:
    Avenging Blade:
      total: 0.67
      efficiency: 0.49
      win: 1.0
      pick: 0.05
      fit: 0.33
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.38
    Dominance:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.36
    Musashi's Dual Swords:
      total: 0.66
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.26
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.62
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.66
  community_ordered:
  - Avenging Blade
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Avenging Blade
  - The Executioner
  - Jotunn's Revenge
  - Dominance
  - Musashi's Dual Swords
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Soul Gem
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
    for this god: Avenging Blade, Rod of Tahuti, Jotunn''s Revenge, Soul Gem, Nimble
    Ring, Gluttonous Grimoire, Death Metal, Silverbranch Bow, The Reaper, Spear of
    Desolation, Tekko-Kagi, Spear of the Magus, Obsidian Shard, Lernaean Bow, The
    Crusher, Hydra''s Lament, Doom Orb, Toxic Blade, The World Stone, Dreamer''s Idol,
    Bragi''s Harp, Pendulum Blade, Avatar''s Parashu, Golden Blade, Bracer of The
    Abyss, Demon Blade, Chronos'' Pendant, Ancient Signet, The Cosmic Horror, Arondight,
    Blood-Bound Book, Oath-Sworn Spear, Runeforged Hammer, Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.69
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.52
    The Executioner:
      total: 0.57
      efficiency: 0.35
      win: 0.75
      pick: 0.33
      fit: 0.59
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.5
    Dominance:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.42
    Musashi's Dual Swords:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.32
    Soul Gem:
      total: 0.51
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.59
  community_ordered:
  - Avenging Blade
  - The Executioner
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Avenging Blade
  - The Executioner
  - Jotunn's Revenge
  - Nimble Ring
  - Dominance
  - Musashi's Dual Swords
  flex_slots:
  - Jotunn's Revenge
  - Nimble Ring
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death Metal, Soul Gem,
    Silverbranch Bow, Lernaean Bow, Gluttonous Grimoire, Tekko-Kagi, The Reaper, Golden
    Blade, Spear of Desolation, Spear of the Magus, Hydra''s Lament, Obsidian Shard,
    Bragi''s Harp, Toxic Blade, Bracer of The Abyss, Qin''s Blade, The Crusher, Demon
    Blade, Chronos'' Pendant, Doom Orb, Ancient Signet, Arondight, The World Stone,
    Blood-Bound Book, Dreamer''s Idol, Runeforged Hammer, Sun Beam Bow, Bancroft''s
    Talon, Pendulum Blade, Berserker''s Shield, Damaru, Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.22
    The Executioner:
      total: 0.53
      efficiency: 0.35
      win: 0.75
      pick: 0.33
      fit: 0.32
    Jotunn's Revenge:
      total: 0.52
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.32
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.34
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.44
    Musashi's Dual Swords:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.31
  community_ordered:
  - Avenging Blade
  - The Executioner
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Avenging Blade
  - Jotunn's Revenge
  - Dominance
  - Spear of Desolation
  - Musashi's Dual Swords
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Soul Gem, Nimble Ring, Spear of Desolation, Death Metal, Hydra''s Lament, Gluttonous
    Grimoire, Chronos'' Pendant, Spear of the Magus, Silverbranch Bow, Lernaean Bow,
    Obsidian Shard, The Reaper, Arondight, Gem of Focus, Tekko-Kagi, Bragi''s Harp,
    Bracer of The Abyss, Pendulum Blade, Doom Orb, Ancient Signet, Golden Blade, Blood-Bound
    Book, The World Stone, Totem of Death, The Crusher, Dreamer''s Idol, Toxic Blade,
    Breastplate of Valor, Bancroft''s Talon, Demon Blade, Genji''s Guard, Qin''s Blade,
    Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.63
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.18
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.48
    Dominance:
      total: 0.56
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.37
    Spear of Desolation:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
    Musashi's Dual Swords:
      total: 0.66
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.27
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.65
  community_ordered:
  - Avenging Blade
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
- source: suggested
  archetype: intelligence
  slot_order:
  - Avenging Blade
  - The Executioner
  - Jotunn's Revenge
  - Dominance
  - Musashi's Dual Swords
  - Soul Gem
  flex_slots:
  - The Executioner
  - Soul Gem
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
    + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble
    Ring, Soul Gem, Death Metal, Gluttonous Grimoire, Spear of Desolation, Spear of
    the Magus, Obsidian Shard, Bragi''s Harp, Bracer of The Abyss, The Reaper, Lernaean
    Bow, Silverbranch Bow, Chronos'' Pendant, Hydra''s Lament, Doom Orb, Tekko-Kagi,
    The World Stone, Ancient Signet, Blood-Bound Book, Dreamer''s Idol, Gem of Focus,
    Bancroft''s Talon, The Crusher, Golden Blade, Arondight, Rod of Asclepius, Book
    of Thoth, Toxic Blade, The Cosmic Horror, Polynomicon, Demon Blade, Typhon’s Heart,
    Pendulum Blade.'
  slot_scores:
    Avenging Blade:
      total: 0.64
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.22
    The Executioner:
      total: 0.52
      efficiency: 0.35
      win: 0.75
      pick: 0.33
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.36
    Dominance:
      total: 0.57
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.39
    Musashi's Dual Swords:
      total: 0.67
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.29
    Soul Gem:
      total: 0.52
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Avenging Blade
  - The Executioner
  - Dominance
  - Musashi's Dual Swords
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Avenging Blade
  - The Executioner
  - Jotunn's Revenge
  - Death Metal
  - Dominance
  - Musashi's Dual Swords
  flex_slots:
  - The Executioner
  - Death Metal
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Death Metal, Nimble Ring, Soul Gem, Gluttonous Grimoire, Spear of Desolation,
    Spear of the Magus, Obsidian Shard, Bragi''s Harp, The Reaper, Lernaean Bow, Tekko-Kagi,
    Hydra''s Lament, Silverbranch Bow, Bracer of The Abyss, Doom Orb, Chronos'' Pendant,
    The World Stone, Ancient Signet, The Crusher, Golden Blade, Dreamer''s Idol, Blood-Bound
    Book, Bancroft''s Talon, Demon Blade, Arondight, Gem of Focus, Toxic Blade, Runeforged
    Hammer, Pendulum Blade, Avatar''s Parashu, Rod of Asclepius, Book of Thoth, Transcendence.'
  slot_scores:
    Avenging Blade:
      total: 0.65
      efficiency: 0.44
      win: 1.0
      pick: 0.05
      fit: 0.27
    The Executioner:
      total: 0.52
      efficiency: 0.35
      win: 0.75
      pick: 0.33
      fit: 0.28
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Death Metal:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.53
    Dominance:
      total: 0.58
      efficiency: 0.45
      win: 0.75
      pick: 0.31
      fit: 0.46
    Musashi's Dual Swords:
      total: 0.68
      efficiency: 0.46
      win: 1.0
      pick: 0.25
      fit: 0.36
  community_ordered:
  - Avenging Blade
  - The Executioner
  - Dominance
  - Musashi's Dual Swords
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Nimble Ring, Death
    Metal, Soul Gem, Lernaean Bow, Gluttonous Grimoire, Silverbranch Bow, Tekko-Kagi,
    The Reaper, Spear of Desolation, Hydra''s Lament, Spear of the Magus, Bragi''s
    Harp, Obsidian Shard, Golden Blade, Demon Blade, Bracer of The Abyss, The Crusher,
    Toxic Blade, Doom Orb, Chronos'' Pendant, Arondight, The World Stone, Ancient
    Signet, Blood-Bound Book, Transcendence, Qin''s Blade, Pendulum Blade, Dreamer''s
    Idol, Damaru, Rage, Runeforged Hammer, Avatar''s Parashu, Bancroft''s Talon.'
  slot_scores:
    Lernaean Bow:
      total: 0.48
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.49
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.37
    Death Metal:
      total: 0.5
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.43
    Rod of Tahuti:
      total: 0.55
      efficiency: 0.86
      win: 0.5
      pick: 0.0
      fit: 0.19
    Soul Gem:
      total: 0.5
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.48
  starter: *id001
---
