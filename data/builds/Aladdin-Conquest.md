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
    pick_rate: 0.68
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.1
      win_rate: 0.86
    - name: Spear of Desolation
      pick_rate: 0.08
      win_rate: 0.33
  - name: Spear of Desolation
    pick_rate: 0.33
    win_rate: 0.58
    alternates:
    - name: Book of Thoth
      pick_rate: 0.25
      win_rate: 0.5
    - name: Transcendence
      pick_rate: 0.18
      win_rate: 0.46
  - name: Book of Thoth
    pick_rate: 0.15
    win_rate: 0.45
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.18
      win_rate: 0.54
    - name: Hydra's Lament
      pick_rate: 0.08
      win_rate: 0.67
  - name: Polynomicon
    pick_rate: 0.28
    win_rate: 0.55
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.25
      win_rate: 0.5
    - name: Heartseeker
      pick_rate: 0.14
      win_rate: 0.5
  - name: Rod of Tahuti
    pick_rate: 0.29
    win_rate: 0.5
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.2
      win_rate: 0.43
    - name: Heartseeker
      pick_rate: 0.1
      win_rate: 0.71
  - name: Obsidian Shard
    pick_rate: 0.24
    win_rate: 0.63
    alternates:
    - name: Dreamer's Idol
      pick_rate: 0.11
      win_rate: 0.43
    - name: Avatar's Parashu
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.46
    win_rate: 0.55
  - name: Conduit Gem
    pick_rate: 0.14
    win_rate: 0.5
  - name: Bumba's Hammer
    pick_rate: 0.11
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/aladdin/
  last_verified: '2026-09-24'
  god_win_rate: 0.5416666666666666
  god_matches_won: 39
  god_matches_played: 72
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: core
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  flex_slots:
  - Obsidian Shard
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    this god: Jotunn''s Revenge, Hydra''s Lament, Soul Gem, Titan''s Bane, The Crusher,
    Pendulum Blade, The Reaper, Spear of the Magus, Arondight, Gluttonous Grimoire,
    Death Metal, Doom Orb, Tekko-Kagi, The World Stone, Chronos'' Pendant, Runeforged
    Hammer, Bragi''s Harp, Avenging Blade, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Lernaean Bow, Shield Splitter, Dominance, Triton''s Conch, Totem of Death,
    Oath-Sworn Spear, Breastplate of Valor, Rod of Asclepius, Barbed Carver, Tyrfing,
    Genji''s Guard, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.9
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.68
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.45
      fit: 0.62
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.63
      fit: 0.42
    Obsidian Shard:
      total: 0.59
      efficiency: 0.54
      win: 0.63
      pick: 0.74
      fit: 0.52
    Avatar's Parashu:
      total: 0.72
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.69
  community_ordered:
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  flex_slots:
  - Hydra's Lament
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
  rationale: 'mana-stack (efficiency + fit + win/pick). Underrated for this god: Jotunn''s
    Revenge, Hydra''s Lament, Soul Gem, Spear of the Magus, Doom Orb, The World Stone,
    Death Metal, Gluttonous Grimoire, Ancient Signet, Chronos'' Pendant, Titan''s
    Bane, The Crusher, The Reaper, Bragi''s Harp, Arondight, Gem of Focus, Pendulum
    Blade, Soul Reaver, The Cosmic Horror, Runeforged Hammer, Rod of Asclepius, Bancroft''s
    Talon, Totem of Death, Triton''s Conch, Tekko-Kagi, Avenging Blade, Blood-Bound
    Book, Jade Scepter, Divine Ruin, Dominance, Wish-Granting Pearl, Helm of Radiance,
    Breastplate of Valor.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.71
    Hydra's Lament:
      total: 0.59
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.63
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.45
      fit: 0.61
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.63
      fit: 0.57
    Obsidian Shard:
      total: 0.6
      efficiency: 0.54
      win: 0.63
      pick: 0.74
      fit: 0.57
    Avatar's Parashu:
      total: 0.69
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.47
  community_ordered:
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  flex_slots:
  - Spear of Desolation
  - Hydra's Lament
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
    god: Jotunn''s Revenge, Hydra''s Lament, Soul Gem, Spear of the Magus, Gluttonous
    Grimoire, Doom Orb, The World Stone, Pendulum Blade, Titan''s Bane, The Crusher,
    Chronos'' Pendant, The Reaper, Death Metal, Arondight, Gem of Focus, The Cosmic
    Horror, Ancient Signet, Tekko-Kagi, Bragi''s Harp, Totem of Death, Runeforged
    Hammer, Rod of Asclepius, Avenging Blade, Blood-Bound Book, Soul Reaver, Jade
    Scepter, Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s Talon,
    Genji''s Guard, Helm of Radiance, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.78
    Hydra's Lament:
      total: 0.58
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.54
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.58
      pick: 0.45
      fit: 0.78
    Rod of Tahuti:
      total: 0.64
      efficiency: 0.86
      win: 0.5
      pick: 0.63
      fit: 0.56
    Obsidian Shard:
      total: 0.61
      efficiency: 0.54
      win: 0.63
      pick: 0.74
      fit: 0.66
    Avatar's Parashu:
      total: 0.7
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.56
  community_ordered:
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Rod of Tahuti
  - Avatar's Parashu
  - Obsidian Shard
  - Amanita Charm
  flex_slots:
  - Hydra's Lament
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
    this god: Amanita Charm, Hydra''s Lament, Jotunn''s Revenge, Shield of the Phoenix,
    Kinetic Cuirass, Soul Gem, Rod of Asclepius, Freya''s Tears, The Reaper, Runeforged
    Hammer, Shifter''s Shield, Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire,
    Shield Splitter, Berserker''s Shield, Eye of the Storm, Ethereal Staff, Yogi''s
    Necklace, Erosion, Eye of Providence, Phoenix Feather, Draconic Scale, Chandra''s
    Grace, Avenging Blade, Lifebinder, Spear of the Magus, Glorious Pridwen, Stone
    of Binding, Helm of Radiance, Midgardian Mail, Daybreak Gavel, Sphere of Negation,
    Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s Hide, Screeching Gargoyle,
    Titan''s Bane.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.45
    Hydra's Lament:
      total: 0.56
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.39
    Rod of Tahuti:
      total: 0.59
      efficiency: 0.86
      win: 0.5
      pick: 0.63
      fit: 0.21
    Avatar's Parashu:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.34
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.74
      fit: 0.31
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.8
  community_ordered:
  - Hydra's Lament
  - Rod of Tahuti
  - Avatar's Parashu
  - Obsidian Shard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  flex_slots:
  - Spear of Desolation
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
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
    for this god: Jotunn''s Revenge, Hydra''s Lament, Soul Gem, Spear of the Magus,
    Titan''s Bane, The Crusher, The Reaper, Pendulum Blade, Gluttonous Grimoire, Doom
    Orb, The World Stone, Tekko-Kagi, Avenging Blade, The Cosmic Horror, Arondight,
    Death Metal, Oath-Sworn Spear, Chronos'' Pendant, Runeforged Hammer, Ancient Signet,
    Gem of Focus, Bragi''s Harp, Screeching Gargoyle, Lernaean Bow, Shield Splitter,
    Dominance, Rod of Asclepius, Totem of Death, Silverbranch Bow, Breastplate of
    Valor, Riptalon, Triton''s Conch, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.93
    Hydra's Lament:
      total: 0.57
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.5
    Spear of Desolation:
      total: 0.6
      efficiency: 0.57
      win: 0.58
      pick: 0.45
      fit: 0.74
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.5
      pick: 0.63
      fit: 0.6
    Obsidian Shard:
      total: 0.62
      efficiency: 0.54
      win: 0.63
      pick: 0.74
      fit: 0.7
    Avatar's Parashu:
      total: 0.74
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.79
  community_ordered:
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Tyrfing
  - Hydra's Lament
  - Nimble Ring
  - Riptalon
  - Obsidian Shard
  - Avatar's Parashu
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
    this god: Hydra''s Lament, Jotunn''s Revenge, Nimble Ring, Riptalon, Tyrfing,
    Silverbranch Bow, Soul Gem, Lernaean Bow, Tekko-Kagi, Golden Blade, Gluttonous
    Grimoire, The Reaper, Toxic Blade, Bragi''s Harp, Spear of the Magus, Dominance,
    Bracer of The Abyss, Qin''s Blade, Titan''s Bane, The Crusher, Doom Orb, Chronos''
    Pendant, Arondight, Sun Beam Bow, The World Stone, Death Metal, Blood-Bound Book,
    Ancient Signet, Pendulum Blade, Berserker''s Shield, Runeforged Hammer, Bancroft''s
    Talon, Dagger of Frenzy, Gem of Focus, Avenging Blade.'
  slot_scores:
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.53
      pick: 0.0
      fit: 0.71
    Hydra's Lament:
      total: 0.55
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.35
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.42
    Riptalon:
      total: 0.52
      efficiency: 0.51
      win: 0.53
      pick: 0.0
      fit: 0.7
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.63
      pick: 0.74
      fit: 0.3
    Avatar's Parashu:
      total: 0.66
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.3
  community_ordered:
  - Hydra's Lament
  - Obsidian Shard
  - Avatar's Parashu
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
  flex_slots:
  - Rod of Tahuti
  - Obsidian Shard
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
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Hydra''s Lament,
    Soul Gem, Chronos'' Pendant, Pendulum Blade, Arondight, Gem of Focus, Spear of
    the Magus, Totem of Death, Gluttonous Grimoire, Breastplate of Valor, Doom Orb,
    Genji''s Guard, The World Stone, Titan''s Bane, The Crusher, The Reaper, Death
    Metal, Ancient Signet, Staff of Myrddin, The Cosmic Horror, Eye of Erebus, Screeching
    Gargoyle, Runeforged Hammer, Chandra''s Grace, Bragi''s Harp, Freya''s Tears,
    Rod of Asclepius, Tekko-Kagi, Avenging Blade, Blood-Bound Book, Soul Reaver, Shield
    of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.85
    Hydra's Lament:
      total: 0.61
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.75
    Spear of Desolation:
      total: 0.61
      efficiency: 0.57
      win: 0.58
      pick: 0.45
      fit: 0.85
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.86
      win: 0.5
      pick: 0.63
      fit: 0.35
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.63
      pick: 0.74
      fit: 0.45
    Avatar's Parashu:
      total: 0.67
      efficiency: 0.45
      win: 1.0
      pick: 0.18
      fit: 0.35
  community_ordered:
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Avatar's Parashu
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
    Underrated for this god: Jotunn''s Revenge, Hydra''s Lament, Soul Gem, Titan''s
    Bane, The Crusher, Pendulum Blade, The Reaper, Spear of the Magus, Arondight,
    Gluttonous Grimoire, Death Metal, Doom Orb, Tekko-Kagi, The World Stone, Chronos''
    Pendant, Runeforged Hammer, Bragi''s Harp, Avenging Blade, Gem of Focus, The Cosmic
    Horror, Ancient Signet, Lernaean Bow, Shield Splitter, Dominance, Triton''s Conch,
    Totem of Death, Oath-Sworn Spear, Breastplate of Valor, Rod of Asclepius, Barbed
    Carver, Tyrfing, Genji''s Guard, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.53
      pick: 0.0
      fit: 0.9
    Transcendence:
      total: 0.46
      efficiency: 0.53
      win: 0.46
      pick: 0.25
      fit: 0.38
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.45
      fit: 0.62
    Hydra's Lament:
      total: 0.6
      efficiency: 0.54
      win: 0.67
      pick: 0.12
      fit: 0.68
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.5
      pick: 0.63
      fit: 0.42
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.5
      pick: 0.23
      fit: 0.89
  community_ordered:
  - Transcendence
  - Spear of Desolation
  - Hydra's Lament
  - Rod of Tahuti
  - Heartseeker
  starter: *id001
---
