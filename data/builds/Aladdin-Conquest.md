---
type: smite-build
god: Aladdin
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Genie's Lamp
    pick_rate: 0.71
    win_rate: 0.55
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.11
      win_rate: 0.25
    - name: Soul Gem
      pick_rate: 0.05
      win_rate: 1.0
  - name: Spear of Desolation
    pick_rate: 0.36
    win_rate: 0.45
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.16
      win_rate: 0.39
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.53
  - name: Book of Thoth
    pick_rate: 0.16
    win_rate: 0.47
    alternates:
    - name: Polynomicon
      pick_rate: 0.13
      win_rate: 0.36
    - name: Spear of Desolation
      pick_rate: 0.12
      win_rate: 0.62
  - name: Rod of Tahuti
    pick_rate: 0.22
    win_rate: 0.52
    alternates:
    - name: Polynomicon
      pick_rate: 0.14
      win_rate: 0.47
    - name: Chronos' Pendant
      pick_rate: 0.1
      win_rate: 0.64
  - name: Obsidian Shard
    pick_rate: 0.28
    win_rate: 0.41
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.46
    - name: Heartseeker
      pick_rate: 0.11
      win_rate: 0.58
  - name: Dreamer's Idol
    pick_rate: 0.09
    win_rate: 0.44
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.17
      win_rate: 0.5
    - name: Rod of Tahuti
      pick_rate: 0.11
      win_rate: 0.4
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.52
    win_rate: 0.43
  - name: Conduit Gem
    pick_rate: 0.21
    win_rate: 0.5
  - name: Bumba's Hammer
    pick_rate: 0.12
    win_rate: 0.46
  source_url: https://smitebrain.com/gods/aladdin/
  last_verified: '2026-09-11'
  god_win_rate: 0.5178571428571429
  god_matches_won: 58
  god_matches_played: 112
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Hydra''s Lament, Titan''s Bane, The Crusher, Pendulum Blade,
    The Reaper, Spear of the Magus, Arondight, Avatar''s Parashu, Gluttonous Grimoire,
    Death Metal, Doom Orb, Tekko-Kagi, The World Stone, Transcendence, Runeforged
    Hammer, Bragi''s Harp, Avenging Blade, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Lernaean Bow, Shield Splitter, Dominance, Triton''s Conch, Totem of Death,
    Oath-Sworn Spear, Breastplate of Valor, Rod of Asclepius, Barbed Carver, Tyrfing,
    Genji''s Guard, Blood-Bound Book.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.47
      pick: 0.25
      fit: 0.1
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.39
      pick: 0.22
      fit: 0.9
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.38
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.89
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.42
    Soul Gem:
      total: 0.74
      efficiency: 0.52
      win: 1.0
      pick: 0.05
      fit: 0.72
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Jotunn's Revenge
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Helm of Radiance — physical protection
    swap_item: Helm of Radiance
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Soul
    Gem, Hydra''s Lament, Spear of the Magus, Doom Orb, The World Stone, Death Metal,
    Gluttonous Grimoire, Ancient Signet, Titan''s Bane, The Crusher, The Reaper, Bragi''s
    Harp, Transcendence, Arondight, Gem of Focus, Pendulum Blade, Avatar''s Parashu,
    Soul Reaver, The Cosmic Horror, Runeforged Hammer, Rod of Asclepius, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Tekko-Kagi, Avenging Blade, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Dominance, Wish-Granting Pearl, Helm of Radiance,
    Breastplate of Valor.'
  slot_scores:
    Chronos' Pendant:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.17
      fit: 0.43
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.39
      pick: 0.22
      fit: 0.71
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.49
      fit: 0.61
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.77
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.57
    Soul Gem:
      total: 0.74
      efficiency: 0.52
      win: 1.0
      pick: 0.05
      fit: 0.71
  community_ordered:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Heartseeker
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability / burst skew (efficiency + fit + win/pick). Underrated for this
    god: Soul Gem, Spear of the Magus, Gluttonous Grimoire, Hydra''s Lament, Doom
    Orb, The World Stone, Pendulum Blade, Titan''s Bane, The Crusher, The Reaper,
    Death Metal, Arondight, Gem of Focus, Avatar''s Parashu, The Cosmic Horror, Ancient
    Signet, Tekko-Kagi, Bragi''s Harp, Totem of Death, Transcendence, Runeforged Hammer,
    Rod of Asclepius, Avenging Blade, Blood-Bound Book, Soul Reaver, Jade Scepter,
    Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon, Genji''s
    Guard, Helm of Radiance, Lernaean Bow.'
  slot_scores:
    Chronos' Pendant:
      total: 0.56
      efficiency: 0.55
      win: 0.64
      pick: 0.17
      fit: 0.44
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.39
      pick: 0.22
      fit: 0.78
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.45
      pick: 0.49
      fit: 0.78
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.76
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.56
    Soul Gem:
      total: 0.76
      efficiency: 0.52
      win: 1.0
      pick: 0.05
      fit: 0.88
  community_ordered:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Heartseeker
  - Rod of Tahuti
  - Amanita Charm
  - Soul Gem
  flex_slots:
  - Chronos' Pendant
  - Jotunn's Revenge
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Soul Gem, Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod
    of Asclepius, Freya''s Tears, The Reaper, Runeforged Hammer, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Shield Splitter, Berserker''s
    Shield, Eye of the Storm, Ethereal Staff, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Hydra''s Lament, Chandra''s Grace, Avenging Blade,
    Lifebinder, Spear of the Magus, Glorious Pridwen, Stone of Binding, Helm of Radiance,
    Midgardian Mail, Daybreak Gavel, Sphere of Negation, Hide of the Nemean Lion,
    Magi''s Cloak, Leviathan''s Hide, Screeching Gargoyle, Titan''s Bane.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.64
      pick: 0.17
      fit: 0.15
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.39
      pick: 0.22
      fit: 0.45
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.54
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.21
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.8
    Soul Gem:
      total: 0.74
      efficiency: 0.52
      win: 1.0
      pick: 0.05
      fit: 0.71
  community_ordered:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Chronos' Pendant
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Soul Gem, Spear of the Magus, Titan''s Bane, The Crusher, The Reaper,
    Pendulum Blade, Gluttonous Grimoire, Avatar''s Parashu, Doom Orb, The World Stone,
    Hydra''s Lament, Tekko-Kagi, Avenging Blade, The Cosmic Horror, Arondight, Death
    Metal, Oath-Sworn Spear, Transcendence, Runeforged Hammer, Ancient Signet, Gem
    of Focus, Bragi''s Harp, Screeching Gargoyle, Lernaean Bow, Shield Splitter, Dominance,
    Rod of Asclepius, Totem of Death, Silverbranch Bow, Breastplate of Valor, Riptalon,
    Triton''s Conch, Blood-Bound Book.'
  slot_scores:
    Chronos' Pendant:
      total: 0.52
      efficiency: 0.55
      win: 0.64
      pick: 0.17
      fit: 0.21
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.39
      pick: 0.22
      fit: 0.93
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.45
      pick: 0.49
      fit: 0.74
    Heartseeker:
      total: 0.58
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.99
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.6
    Soul Gem:
      total: 0.76
      efficiency: 0.52
      win: 1.0
      pick: 0.05
      fit: 0.84
  community_ordered:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Chronos' Pendant
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Rod of Tahuti
  - Heartseeker
  flex_slots:
  - Riptalon
  - Tyrfing
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
    this god: Soul Gem, Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Lernaean
    Bow, Tekko-Kagi, Golden Blade, Gluttonous Grimoire, The Reaper, Toxic Blade, Hydra''s
    Lament, Bragi''s Harp, Spear of the Magus, Dominance, Bracer of The Abyss, Qin''s
    Blade, Titan''s Bane, The Crusher, Doom Orb, Arondight, Sun Beam Bow, The World
    Stone, Death Metal, Blood-Bound Book, Ancient Signet, Pendulum Blade, Transcendence,
    Berserker''s Shield, Runeforged Hammer, Avatar''s Parashu, Bancroft''s Talon,
    Dagger of Frenzy, Gem of Focus, Avenging Blade.'
  slot_scores:
    Chronos' Pendant:
      total: 0.51
      efficiency: 0.55
      win: 0.64
      pick: 0.17
      fit: 0.15
    Tyrfing:
      total: 0.49
      efficiency: 0.48
      win: 0.47
      pick: 0.0
      fit: 0.71
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.47
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.5
      efficiency: 0.51
      win: 0.47
      pick: 0.0
      fit: 0.7
    Rod of Tahuti:
      total: 0.58
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.2
    Heartseeker:
      total: 0.51
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.5
  community_ordered:
  - Chronos' Pendant
  - Rod of Tahuti
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  flex_slots:
  - Spear of Desolation
  - Heartseeker
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Hydra''s Lament, Pendulum
    Blade, Arondight, Gem of Focus, Spear of the Magus, Totem of Death, Gluttonous
    Grimoire, Breastplate of Valor, Doom Orb, Genji''s Guard, The World Stone, Titan''s
    Bane, The Crusher, The Reaper, Death Metal, Ancient Signet, Staff of Myrddin,
    Avatar''s Parashu, The Cosmic Horror, Eye of Erebus, Transcendence, Screeching
    Gargoyle, Runeforged Hammer, Chandra''s Grace, Bragi''s Harp, Freya''s Tears,
    Rod of Asclepius, Tekko-Kagi, Avenging Blade, Blood-Bound Book, Soul Reaver, Shield
    of the Phoenix.'
  slot_scores:
    Chronos' Pendant:
      total: 0.59
      efficiency: 0.55
      win: 0.64
      pick: 0.17
      fit: 0.65
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.39
      pick: 0.22
      fit: 0.85
    Spear of Desolation:
      total: 0.56
      efficiency: 0.57
      win: 0.45
      pick: 0.49
      fit: 0.85
    Heartseeker:
      total: 0.52
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.55
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.35
    Soul Gem:
      total: 0.78
      efficiency: 0.52
      win: 1.0
      pick: 0.05
      fit: 0.95
  community_ordered:
  - Chronos' Pendant
  - Jotunn's Revenge
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
  - Soul Gem
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Spear of Desolation
  - Hydra's Lament
  - Rod of Tahuti
  - Heartseeker
  flex_slots:
  - Hydra's Lament
  - Transcendence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Hydra''s Lament, Soul Gem, Titan''s Bane, The Crusher,
    Pendulum Blade, The Reaper, Spear of the Magus, Arondight, Avatar''s Parashu,
    Gluttonous Grimoire, Death Metal, Doom Orb, Tekko-Kagi, The World Stone, Transcendence,
    Runeforged Hammer, Bragi''s Harp, Avenging Blade, Gem of Focus, The Cosmic Horror,
    Ancient Signet, Lernaean Bow, Shield Splitter, Dominance, Triton''s Conch, Totem
    of Death, Oath-Sworn Spear, Breastplate of Valor, Rod of Asclepius, Barbed Carver,
    Tyrfing, Genji''s Guard, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.39
      pick: 0.22
      fit: 0.9
    Transcendence:
      total: 0.45
      efficiency: 0.53
      win: 0.47
      pick: 0.0
      fit: 0.38
    Spear of Desolation:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.49
      fit: 0.62
    Hydra's Lament:
      total: 0.5
      efficiency: 0.54
      win: 0.47
      pick: 0.0
      fit: 0.68
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.52
      pick: 0.37
      fit: 0.42
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.58
      pick: 0.24
      fit: 0.89
  community_ordered:
  - Jotunn's Revenge
  - Spear of Desolation
  - Rod of Tahuti
  - Heartseeker
  starter: *id001
---
