---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.02
  aspect_win_rate: 0.4
  slot_order:
  - name: Devourer's Gauntlet
    pick_rate: 0.67
    win_rate: 0.55
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.64
    - name: The Crusher
      pick_rate: 0.05
      win_rate: 0.62
  - name: Sanguine Lash
    pick_rate: 0.46
    win_rate: 0.53
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.5
    - name: Brawler’s Beat Stick
      pick_rate: 0.06
      win_rate: 0.8
  - name: The Reaper
    pick_rate: 0.14
    win_rate: 0.72
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.63
    - name: Umbral Link
      pick_rate: 0.13
      win_rate: 0.53
  - name: Freya's Tears
    pick_rate: 0.23
    win_rate: 0.44
    alternates:
    - name: Gluttonous Grimoire
      pick_rate: 0.1
      win_rate: 0.71
    - name: Brawler’s Beat Stick
      pick_rate: 0.09
      win_rate: 0.53
  - name: Blinking Abyss
    pick_rate: 0.09
    win_rate: 0.58
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.61
    - name: Sundering Echo
      pick_rate: 0.09
      win_rate: 0.72
  - name: Sundering Echo
    pick_rate: 0.07
    win_rate: 0.6
    alternates:
    - name: Sage's Ring
      pick_rate: 0.05
      win_rate: 0.38
    - name: Heartseeker
      pick_rate: 0.04
      win_rate: 0.5
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.43
    win_rate: 0.56
  - name: Bluestone Pendant
    pick_rate: 0.23
    win_rate: 0.52
  - name: Hunter's Cowl
    pick_rate: 0.1
    win_rate: 0.67
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-10-24'
  god_win_rate: 0.5625
  god_matches_won: 135
  god_matches_played: 240
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-24'
  god_matches_analyzed: 3785
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Shifter''s Shield, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, The Crusher, Avenging Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Draconic
    Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s
    Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian
    Mail, Triton''s Conch, Stone of Binding, Dominance, Hide of the Nemean Lion, Spear
    of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter, Void
    Shield, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.17
      fit: 0.42
    Shifter's Shield:
      total: 0.55
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.45
  community_ordered:
  - Gluttonous Grimoire
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - The Reaper
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shifter''s Shield, Rod of Tahuti, Berserker''s Shield,
    Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Rod of Asclepius, Runeforged
    Hammer, Shield Splitter, Eye of the Storm, Soul Gem, Erosion, Genji''s Guard,
    Ethereal Staff, Breastplate of Valor, Eye of Providence, Yogi''s Necklace, Draconic
    Scale, Phoenix Feather, Avenging Blade, Pharaoh''s Curse, Shogun''s Ofuda, Lernaean
    Bow, Hydra''s Lament, Lifebinder, Stone of Binding, Midgardian Mail, Helm of Radiance,
    Chandra''s Grace, Daybreak Gavel, Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s
    Hide, Sphere of Negation, Void Shield, Stampede, Ancile, Heartseeker.'
  slot_scores:
    Berserker's Shield:
      total: 0.56
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.31
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.64
    The Reaper:
      total: 0.59
      efficiency: 0.5
      win: 0.72
      pick: 0.22
      fit: 0.57
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.54
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.84
  community_ordered:
  - The Reaper
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  - Rod of Tahuti
  flex_slots:
  - Shifter's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Stone of Binding — physical protection
    swap_item: Stone of Binding
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, The Crusher, Shifter''s Shield,
    Berserker''s Shield, Avenging Blade, Amanita Charm, Spear of the Magus, Stone
    of Binding, Obsidian Shard, Spear of Desolation, Tekko-Kagi, Runeforged Hammer,
    Titan''s Bane, Kinetic Cuirass, Soul Gem, Void Shield, Heartseeker, Screeching
    Gargoyle, Void Stone, Genji''s Guard, Breastplate of Valor, Shield Splitter, Doom
    Orb, Eye of the Storm, The World Stone, Avatar''s Parashu, Hydra''s Lament, Lernaean
    Bow, Dreamer''s Idol, Pendulum Blade, Nimble Ring, Daybreak Gavel, Helm of Radiance,
    Erosion, Pharaoh''s Curse, Rod of Asclepius, Eye of Providence, Shield of the
    Phoenix.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.61
      efficiency: 0.55
      win: 0.71
      pick: 0.17
      fit: 0.63
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.31
    The Crusher:
      total: 0.54
      efficiency: 0.47
      win: 0.62
      pick: 0.05
      fit: 0.63
    Rod of Tahuti:
      total: 0.6
      efficiency: 0.86
      win: 0.55
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Gluttonous Grimoire
  - Shifter's Shield
  - The Crusher
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Golden Blade
  - Jotunn's Revenge
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Shifter''s Shield, Nimble Ring,
    Golden Blade, Jotunn''s Revenge, Amanita Charm, Tyrfing, Riptalon, Kinetic Cuirass,
    Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Toxic Blade, Pharaoh''s Curse,
    Genji''s Guard, Breastplate of Valor, Soul Gem, Shogun''s Ofuda, Shield Splitter,
    Tekko-Kagi, Bragi''s Harp, Eye of the Storm, Hydra''s Lament, Daybreak Gavel,
    Dominance, Avenging Blade, Helm of Radiance, Bracer of The Abyss, Rod of Asclepius,
    Spear of the Magus, Erosion, Shield of the Phoenix, Eye of Providence, Qin''s
    Blade, Vital Amplifier, Draconic Scale, Obsidian Shard, Heartseeker.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.19
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.36
    Gluttonous Grimoire:
      total: 0.6
      efficiency: 0.6
      win: 0.71
      pick: 0.17
      fit: 0.38
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.29
  community_ordered:
  - Gluttonous Grimoire
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  flex_slots:
  - Shifter's Shield
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Genji''s Guard, Breastplate of Valor, Shifter''s Shield, Berserker''s Shield,
    Amanita Charm, Spear of Desolation, Hydra''s Lament, Shield of the Phoenix, Soul
    Gem, Chronos'' Pendant, Kinetic Cuirass, Screeching Gargoyle, Runeforged Hammer,
    Arondight, Gem of Focus, Gladiator''s Shield, Nimble Ring, Eye of Erebus, Helm
    of Radiance, Rod of Asclepius, Shield Splitter, Spear of the Magus, Prophetic
    Cloak, Chandra''s Grace, Eye of the Storm, Daybreak Gavel, Obsidian Shard, Erosion,
    Pharaoh''s Curse, Jade Scepter, Lernaean Bow, Eye of Providence, Wish-Granting
    Pearl, Avenging Blade, Totem of Death, Draconic Scale, Pendulum Blade, Shogun''s
    Ofuda.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.55
      pick: 0.0
      fit: 0.44
    Berserker's Shield:
      total: 0.53
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.49
    Gluttonous Grimoire:
      total: 0.58
      efficiency: 0.55
      win: 0.71
      pick: 0.17
      fit: 0.39
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.64
      pick: 0.12
      fit: 0.31
  community_ordered:
  - Gluttonous Grimoire
  - Shifter's Shield
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
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Shifter''s Shield, Avenging Blade, Genji''s Guard, Lernaean Bow, Breastplate
    of Valor, Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker,
    Draconic Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi,
    Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance,
    Midgardian Mail, Triton''s Conch, Stone of Binding, Dominance, Hide of the Nemean
    Lion, Spear of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade
    Scepter, The Crusher, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.52
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.57
      win: 0.55
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  starter: *id001
---
