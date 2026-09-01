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
    pick_rate: 0.73
    win_rate: 0.53
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.13
      win_rate: 0.52
    - name: Jotunn's Revenge
      pick_rate: 0.06
      win_rate: 0.67
  - name: Spear of Desolation
    pick_rate: 0.37
    win_rate: 0.5
    alternates:
    - name: Jotunn's Revenge
      pick_rate: 0.21
      win_rate: 0.63
    - name: Book of Thoth
      pick_rate: 0.15
      win_rate: 0.53
  - name: Book of Thoth
    pick_rate: 0.2
    win_rate: 0.51
    alternates:
    - name: Transcendence
      pick_rate: 0.15
      win_rate: 0.58
    - name: Spear of Desolation
      pick_rate: 0.09
      win_rate: 0.44
  - name: Polynomicon
    pick_rate: 0.2
    win_rate: 0.49
    alternates:
    - name: Rod of Tahuti
      pick_rate: 0.14
      win_rate: 0.48
    - name: Heartseeker
      pick_rate: 0.08
      win_rate: 0.61
  - name: Rod of Tahuti
    pick_rate: 0.33
    win_rate: 0.58
    alternates:
    - name: Heartseeker
      pick_rate: 0.19
      win_rate: 0.52
    - name: Obsidian Shard
      pick_rate: 0.13
      win_rate: 0.42
  - name: Obsidian Shard
    pick_rate: 0.21
    win_rate: 0.57
    alternates:
    - name: Evil Eye
      pick_rate: 0.07
      win_rate: 0.33
    - name: Titan's Bane
      pick_rate: 0.06
      win_rate: 0.53
  community_starters:
  - name: Archmage's Gem
    pick_rate: 0.48
    win_rate: 0.55
  - name: Conduit Gem
    pick_rate: 0.17
    win_rate: 0.44
  - name: Bluestone Brooch
    pick_rate: 0.11
    win_rate: 0.74
  source_url: https://smitebrain.com/gods/aladdin/
  last_verified: '2026-09-01'
  god_win_rate: 0.5415472779369628
  god_matches_won: 189
  god_matches_played: 349
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-09-01'
  god_matches_analyzed: 8200
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
  - Obsidian Shard
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
    this god: Hydra''s Lament, Soul Gem, The Crusher, Pendulum Blade, The Reaper,
    Spear of the Magus, Arondight, Avatar''s Parashu, Gluttonous Grimoire, Death Metal,
    Doom Orb, Tekko-Kagi, The World Stone, Dreamer''s Idol, Chronos'' Pendant, Runeforged
    Hammer, Bragi''s Harp, Avenging Blade, Gem of Focus, The Cosmic Horror, Ancient
    Signet, Lernaean Bow, Shield Splitter, Dominance, Triton''s Conch, Totem of Death,
    Oath-Sworn Spear, Breastplate of Valor, Rod of Asclepius, Barbed Carver, Tyrfing,
    Genji''s Guard, Blood-Bound Book.'
  slot_scores:
    Book of Thoth:
      total: 0.44
      efficiency: 0.51
      win: 0.51
      pick: 0.31
      fit: 0.1
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.9
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.58
      pick: 0.23
      fit: 0.38
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.52
      pick: 0.41
      fit: 0.89
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.42
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.57
      pick: 0.65
      fit: 0.52
  starter: &id001
    base: Conduit Gem
    upgrade: Archmage's Gem
- source: suggested
  archetype: mana-stack
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    Gluttonous Grimoire, Ancient Signet, Chronos'' Pendant, The Crusher, Dreamer''s
    Idol, The Reaper, Bragi''s Harp, Arondight, Gem of Focus, Pendulum Blade, Avatar''s
    Parashu, Soul Reaver, The Cosmic Horror, Runeforged Hammer, Rod of Asclepius,
    Bancroft''s Talon, Totem of Death, Triton''s Conch, Tekko-Kagi, Avenging Blade,
    Blood-Bound Book, Jade Scepter, Divine Ruin, Dominance, Wish-Granting Pearl, Helm
    of Radiance, Breastplate of Valor.'
  slot_scores:
    Book of Thoth:
      total: 0.48
      efficiency: 0.51
      win: 0.51
      pick: 0.31
      fit: 0.39
    Jotunn's Revenge:
      total: 0.66
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.71
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.58
      pick: 0.23
      fit: 0.39
    Heartseeker:
      total: 0.53
      efficiency: 0.47
      win: 0.52
      pick: 0.41
      fit: 0.77
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.57
    Obsidian Shard:
      total: 0.56
      efficiency: 0.54
      win: 0.57
      pick: 0.65
      fit: 0.57
  starter: *id001
- source: suggested
  archetype: burst
  slot_order:
  - Jotunn's Revenge
  - Spear of Desolation
  - Spear of the Magus
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Soul Gem
  - Spear of the Magus
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
    Orb, The World Stone, Pendulum Blade, The Crusher, Dreamer''s Idol, Chronos''
    Pendant, The Reaper, Death Metal, Arondight, Gem of Focus, Avatar''s Parashu,
    The Cosmic Horror, Ancient Signet, Tekko-Kagi, Bragi''s Harp, Totem of Death,
    Runeforged Hammer, Rod of Asclepius, Avenging Blade, Blood-Bound Book, Soul Reaver,
    Jade Scepter, Divine Ruin, Triton''s Conch, Breastplate of Valor, Bancroft''s
    Talon, Genji''s Guard, Helm of Radiance, Lernaean Bow.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.67
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.78
    Spear of Desolation:
      total: 0.57
      efficiency: 0.57
      win: 0.5
      pick: 0.5
      fit: 0.78
    Spear of the Magus:
      total: 0.53
      efficiency: 0.6
      win: 0.53
      pick: 0.0
      fit: 0.56
    Rod of Tahuti:
      total: 0.68
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.56
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.57
      pick: 0.65
      fit: 0.66
    Soul Gem:
      total: 0.55
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.88
  starter: *id001
- source: suggested
  archetype: bruiser
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Shield of the Phoenix
  - Transcendence
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Soul Gem, Rod
    of Asclepius, Freya''s Tears, The Reaper, Runeforged Hammer, Shifter''s Shield,
    Genji''s Guard, Breastplate of Valor, Gluttonous Grimoire, Shield Splitter, Berserker''s
    Shield, Eye of the Storm, Ethereal Staff, Yogi''s Necklace, Erosion, Eye of Providence,
    Phoenix Feather, Draconic Scale, Hydra''s Lament, Chandra''s Grace, Avenging Blade,
    Lifebinder, Spear of the Magus, Glorious Pridwen, Stone of Binding, Helm of Radiance,
    Midgardian Mail, Daybreak Gavel, Sphere of Negation, Hide of the Nemean Lion,
    Magi''s Cloak, Leviathan''s Hide, Screeching Gargoyle.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.51
      pick: 0.31
      fit: 0.05
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.45
    Shield of the Phoenix:
      total: 0.54
      efficiency: 0.53
      win: 0.53
      pick: 0.0
      fit: 0.75
    Transcendence:
      total: 0.49
      efficiency: 0.53
      win: 0.58
      pick: 0.23
      fit: 0.19
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.21
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.53
      pick: 0.0
      fit: 0.8
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Heartseeker
  - Rod of Tahuti
  - Obsidian Shard
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    for this god: Soul Gem, Spear of the Magus, The Crusher, The Reaper, Pendulum
    Blade, Gluttonous Grimoire, Avatar''s Parashu, Doom Orb, The World Stone, Dreamer''s
    Idol, Hydra''s Lament, Tekko-Kagi, Avenging Blade, The Cosmic Horror, Arondight,
    Death Metal, Oath-Sworn Spear, Chronos'' Pendant, Runeforged Hammer, Ancient Signet,
    Gem of Focus, Bragi''s Harp, Screeching Gargoyle, Lernaean Bow, Shield Splitter,
    Dominance, Rod of Asclepius, Totem of Death, Silverbranch Bow, Breastplate of
    Valor, Riptalon, Triton''s Conch, Blood-Bound Book.'
  slot_scores:
    Book of Thoth:
      total: 0.43
      efficiency: 0.51
      win: 0.51
      pick: 0.31
      fit: 0.07
    Jotunn's Revenge:
      total: 0.69
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.93
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.58
      pick: 0.23
      fit: 0.26
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.52
      pick: 0.41
      fit: 0.99
    Rod of Tahuti:
      total: 0.69
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.6
    Obsidian Shard:
      total: 0.58
      efficiency: 0.54
      win: 0.57
      pick: 0.65
      fit: 0.7
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Tyrfing
  - Nimble Ring
  - Riptalon
  - Rod of Tahuti
  flex_slots:
  - Tyrfing
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
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Nimble Ring, Riptalon, Tyrfing, Silverbranch Bow, Soul Gem, Lernaean
    Bow, Tekko-Kagi, Golden Blade, Gluttonous Grimoire, The Reaper, Toxic Blade, Hydra''s
    Lament, Bragi''s Harp, Spear of the Magus, Dominance, Bracer of The Abyss, Qin''s
    Blade, The Crusher, Doom Orb, Chronos'' Pendant, Arondight, Sun Beam Bow, The
    World Stone, Death Metal, Blood-Bound Book, Ancient Signet, Pendulum Blade, Dreamer''s
    Idol, Berserker''s Shield, Runeforged Hammer, Avatar''s Parashu, Bancroft''s Talon,
    Dagger of Frenzy, Gem of Focus, Avenging Blade.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.39
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.23
      fit: 0.15
    Tyrfing:
      total: 0.51
      efficiency: 0.48
      win: 0.53
      pick: 0.0
      fit: 0.71
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
    Rod of Tahuti:
      total: 0.63
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.2
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Jotunn's Revenge
  - Hydra's Lament
  - Spear of Desolation
  - Rod of Tahuti
  - Obsidian Shard
  - Soul Gem
  flex_slots:
  - Obsidian Shard
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Soul Gem, Hydra''s Lament, Chronos''
    Pendant, Pendulum Blade, Arondight, Gem of Focus, Spear of the Magus, Totem of
    Death, Gluttonous Grimoire, Breastplate of Valor, Doom Orb, Genji''s Guard, The
    World Stone, The Crusher, Dreamer''s Idol, The Reaper, Death Metal, Ancient Signet,
    Staff of Myrddin, Avatar''s Parashu, The Cosmic Horror, Eye of Erebus, Screeching
    Gargoyle, Runeforged Hammer, Chandra''s Grace, Bragi''s Harp, Freya''s Tears,
    Rod of Asclepius, Tekko-Kagi, Avenging Blade, Blood-Bound Book, Soul Reaver, Shield
    of the Phoenix.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.85
    Hydra's Lament:
      total: 0.54
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.75
    Spear of Desolation:
      total: 0.58
      efficiency: 0.57
      win: 0.5
      pick: 0.5
      fit: 0.85
    Rod of Tahuti:
      total: 0.65
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.35
    Obsidian Shard:
      total: 0.55
      efficiency: 0.54
      win: 0.57
      pick: 0.65
      fit: 0.45
    Soul Gem:
      total: 0.56
      efficiency: 0.52
      win: 0.53
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Transcendence
  - Hydra's Lament
  - Spear of Desolation
  - Heartseeker
  - Rod of Tahuti
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
    Underrated for this god: Hydra''s Lament, Soul Gem, The Crusher, Pendulum Blade,
    The Reaper, Spear of the Magus, Arondight, Avatar''s Parashu, Gluttonous Grimoire,
    Death Metal, Doom Orb, Tekko-Kagi, The World Stone, Dreamer''s Idol, Chronos''
    Pendant, Runeforged Hammer, Bragi''s Harp, Avenging Blade, Gem of Focus, The Cosmic
    Horror, Ancient Signet, Lernaean Bow, Shield Splitter, Dominance, Triton''s Conch,
    Totem of Death, Oath-Sworn Spear, Breastplate of Valor, Rod of Asclepius, Barbed
    Carver, Tyrfing, Genji''s Guard, Blood-Bound Book.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.68
      efficiency: 0.72
      win: 0.63
      pick: 0.29
      fit: 0.9
    Transcendence:
      total: 0.51
      efficiency: 0.53
      win: 0.58
      pick: 0.23
      fit: 0.38
    Hydra's Lament:
      total: 0.53
      efficiency: 0.54
      win: 0.53
      pick: 0.0
      fit: 0.68
    Spear of Desolation:
      total: 0.54
      efficiency: 0.57
      win: 0.5
      pick: 0.5
      fit: 0.62
    Heartseeker:
      total: 0.55
      efficiency: 0.47
      win: 0.52
      pick: 0.41
      fit: 0.89
    Rod of Tahuti:
      total: 0.66
      efficiency: 0.86
      win: 0.58
      pick: 0.71
      fit: 0.42
  starter: *id001
---
