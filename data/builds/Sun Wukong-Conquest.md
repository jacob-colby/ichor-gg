---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.36
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.36
    win_rate: 0.51
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.67
    - name: Book of Thoth
      pick_rate: 0.12
      win_rate: 0.5
  - name: Jotunn's Revenge
    pick_rate: 0.13
    win_rate: 0.63
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.09
      win_rate: 0.55
    - name: Lifebinder
      pick_rate: 0.08
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.47
    - name: Genji's Guard
      pick_rate: 0.11
      win_rate: 0.62
  - name: Brawler’s Beat Stick
    pick_rate: 0.18
    win_rate: 0.7
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.3
  - name: Heartseeker
    pick_rate: 0.1
    win_rate: 0.64
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.07
      win_rate: 0.57
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.43
  - name: Engraved Guard
    pick_rate: 0.06
    win_rate: 0.0
    alternates:
    - name: Heartseeker
      pick_rate: 0.04
      win_rate: 0.67
    - name: Jotunn's Revenge
      pick_rate: 0.04
      win_rate: 0.33
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.48
    win_rate: 0.53
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.56
  - name: Conduit Gem
    pick_rate: 0.1
    win_rate: 0.42
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-09-24'
  god_win_rate: 0.5166666666666667
  god_matches_won: 62
  god_matches_played: 120
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-24'
  god_matches_analyzed: 1954
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Runeforged Hammer,
    Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade, Gluttonous
    Grimoire, Lernaean Bow, Breastplate of Valor, Hydra''s Lament, Erosion, Pharaoh''s
    Curse, Eye of Providence, Draconic Scale, Shogun''s Ofuda, Golden Blade, Shield
    of the Phoenix, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble
    Ring, Helm of Radiance, Midgardian Mail, Triton''s Conch, Stone of Binding, Dominance,
    Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter,
    The Crusher, Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.62
      pick: 0.17
      fit: 0.17
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.18
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Shield of the Phoenix
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Kinetic Cuirass,
    Shield of the Phoenix, Rod of Asclepius, Runeforged Hammer, Shield Splitter, Eye
    of the Storm, Soul Gem, Erosion, Ethereal Staff, The Reaper, Breastplate of Valor,
    Eye of Providence, Yogi''s Necklace, Lifebinder, Draconic Scale, Phoenix Feather,
    Gluttonous Grimoire, Avenging Blade, Pharaoh''s Curse, Shogun''s Ofuda, Lernaean
    Bow, Hydra''s Lament, Stone of Binding, Midgardian Mail, Helm of Radiance, Chandra''s
    Grace, Daybreak Gavel, Magi''s Cloak, Leviathan''s Hide, Sphere of Negation, Void
    Shield, Stampede, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.62
      pick: 0.17
      fit: 0.2
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.63
      pick: 0.18
      fit: 0.31
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.64
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.71
    Amanita Charm:
      total: 0.62
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Gluttonous Grimoire
  - Heartseeker
  - Rod of Tahuti
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Gluttonous Grimoire, Berserker''s Shield, Avenging
    Blade, Amanita Charm, Spear of the Magus, Stone of Binding, Obsidian Shard, Spear
    of Desolation, Tekko-Kagi, Runeforged Hammer, Titan''s Bane, Kinetic Cuirass,
    The Crusher, Soul Gem, Void Shield, Screeching Gargoyle, The Reaper, Void Stone,
    Breastplate of Valor, Shield Splitter, Doom Orb, Eye of the Storm, The World Stone,
    Avatar''s Parashu, Hydra''s Lament, Lernaean Bow, Dreamer''s Idol, Pendulum Blade,
    Nimble Ring, Daybreak Gavel, Helm of Radiance, Erosion, Pharaoh''s Curse, Rod
    of Asclepius, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Book of Thoth:
      total: 0.42
      efficiency: 0.51
      win: 0.5
      pick: 0.12
      fit: 0.04
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.63
      pick: 0.18
      fit: 0.56
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.18
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.63
    Heartseeker:
      total: 0.57
      efficiency: 0.47
      win: 0.64
      pick: 0.22
      fit: 0.73
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.86
      win: 0.58
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Book of Thoth
  - Jotunn's Revenge
  - Heartseeker
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Genji's Guard
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
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Nimble Ring, Golden Blade, Amanita
    Charm, Gluttonous Grimoire, Tyrfing, Riptalon, Kinetic Cuirass, Runeforged Hammer,
    Lernaean Bow, Silverbranch Bow, Toxic Blade, Pharaoh''s Curse, Breastplate of
    Valor, Soul Gem, Shogun''s Ofuda, Shield Splitter, Tekko-Kagi, Bragi''s Harp,
    Eye of the Storm, Hydra''s Lament, The Reaper, Daybreak Gavel, Dominance, Avenging
    Blade, Helm of Radiance, Bracer of The Abyss, Rod of Asclepius, Spear of the Magus,
    Erosion, Shield of the Phoenix, Eye of Providence, Qin''s Blade, Vital Amplifier,
    Draconic Scale, Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.65
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.62
      pick: 0.17
      fit: 0.11
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.63
      pick: 0.18
      fit: 0.19
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.36
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.29
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Brawler’s Beat Stick — anti-heal
    swap_item: Brawler’s Beat Stick
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Berserker''s Shield, Amanita Charm, Spear of Desolation, Hydra''s Lament, Shield
    of the Phoenix, Soul Gem, Chronos'' Pendant, Kinetic Cuirass, Screeching Gargoyle,
    Gluttonous Grimoire, Runeforged Hammer, Arondight, Gem of Focus, Gladiator''s
    Shield, Nimble Ring, Eye of Erebus, Helm of Radiance, Rod of Asclepius, Shield
    Splitter, Spear of the Magus, Prophetic Cloak, Chandra''s Grace, Eye of the Storm,
    Daybreak Gavel, Obsidian Shard, Erosion, Pharaoh''s Curse, Jade Scepter, Lernaean
    Bow, Eye of Providence, Wish-Granting Pearl, Avenging Blade, Totem of Death, Draconic
    Scale, Pendulum Blade, Shogun''s Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.62
      pick: 0.17
      fit: 0.44
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.63
      pick: 0.18
      fit: 0.49
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.56
      pick: 0.36
      fit: 0.52
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Runeforged Hammer
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Eye of the Storm — magical protection
    swap_item: Eye of the Storm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Runeforged
    Hammer, Kinetic Cuirass, Shield Splitter, Eye of the Storm, Avenging Blade, Gluttonous
    Grimoire, Lernaean Bow, Breastplate of Valor, Hydra''s Lament, Erosion, Pharaoh''s
    Curse, Eye of Providence, Draconic Scale, Shogun''s Ofuda, Golden Blade, Shield
    of the Phoenix, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble
    Ring, Helm of Radiance, Midgardian Mail, Triton''s Conch, Stone of Binding, Dominance,
    Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter,
    The Crusher, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.63
      pick: 0.18
      fit: 0.37
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.58
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Jotunn's Revenge
  starter: *id001
---
