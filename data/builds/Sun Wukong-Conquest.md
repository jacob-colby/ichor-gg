---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.12
  aspect_win_rate: 0.5
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.43
    win_rate: 0.45
    alternates:
    - name: Scepter of Dominion
      pick_rate: 0.1
      win_rate: 0.14
    - name: Runeforged Hammer
      pick_rate: 0.07
      win_rate: 0.2
  - name: Prophetic Cloak
    pick_rate: 0.1
    win_rate: 0.43
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.75
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.4
  - name: Freya's Tears
    pick_rate: 0.2
    win_rate: 0.38
    alternates:
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.38
    - name: Breastplate of Valor
      pick_rate: 0.08
      win_rate: 0.6
  - name: Spirit Robe
    pick_rate: 0.1
    win_rate: 0.33
    alternates:
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.71
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 0.0
  - name: Draconic Scale
    pick_rate: 0.05
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.13
    - name: Shifter's Shield
      pick_rate: 0.07
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.33
    alternates:
    - name: Void Shard
      pick_rate: 0.05
      win_rate: 0.0
    - name: Veve Charm
      pick_rate: 0.05
      win_rate: 1.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.28
    win_rate: 0.58
  - name: Bluestone Pendant
    pick_rate: 0.15
    win_rate: 0.7
  - name: Heroism
    pick_rate: 0.1
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-08-27'
  god_win_rate: 0.417910447761194
  god_matches_won: 28
  god_matches_played: 67
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-27'
  god_matches_analyzed: 2301
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Draconic Scale
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
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Breastplate of Valor, Rod of Tahuti, Jotunn''s Revenge,
    Berserker''s Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Hydra''s Lament, Erosion,
    Pharaoh''s Curse, Eye of Providence, Heartseeker, Shogun''s Ofuda, Golden Blade,
    Shield of the Phoenix, Tekko-Kagi, Bragi''s Harp, Rod of Asclepius, Daybreak Gavel,
    Nimble Ring, Helm of Radiance, Midgardian Mail, Triton''s Conch, Stone of Binding,
    Dominance, Hide of the Nemean Lion, Spear of the Magus, Titan''s Bane, Death Metal,
    Leviathan''s Hide, Jade Scepter, The Crusher, Void Shield, Runeforged Hammer.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.17
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.37
    Shifter's Shield:
      total: 0.48
      efficiency: 0.55
      win: 0.45
      pick: 0.43
      fit: 0.45
    Draconic Scale:
      total: 0.55
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.45
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.45
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Shifter's Shield
  - Draconic Scale
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
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
    this god: Draconic Scale, Breastplate of Valor, Amanita Charm, Rod of Tahuti,
    Berserker''s Shield, Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix,
    Rod of Asclepius, Shield Splitter, Eye of the Storm, Soul Gem, Erosion, Ethereal
    Staff, The Reaper, Eye of Providence, Yogi''s Necklace, Phoenix Feather, Gluttonous
    Grimoire, Avenging Blade, Pharaoh''s Curse, Shogun''s Ofuda, Lernaean Bow, Hydra''s
    Lament, Lifebinder, Stone of Binding, Midgardian Mail, Helm of Radiance, Chandra''s
    Grace, Daybreak Gavel, Hide of the Nemean Lion, Magi''s Cloak, Leviathan''s Hide,
    Sphere of Negation, Void Shield, Stampede, Heartseeker, Ancile, Runeforged Hammer.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.2
    Jotunn's Revenge:
      total: 0.47
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.31
    Shifter's Shield:
      total: 0.5
      efficiency: 0.55
      win: 0.45
      pick: 0.43
      fit: 0.54
    Draconic Scale:
      total: 0.56
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.54
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.84
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Gluttonous Grimoire
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Gluttonous Grimoire
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
    for this god: Rod of Tahuti, Breastplate of Valor, Jotunn''s Revenge, Gluttonous
    Grimoire, Berserker''s Shield, Avenging Blade, Amanita Charm, Heartseeker, Spear
    of the Magus, Stone of Binding, Obsidian Shard, Spear of Desolation, Tekko-Kagi,
    Titan''s Bane, Kinetic Cuirass, The Crusher, Soul Gem, Void Shield, Screeching
    Gargoyle, The Reaper, Void Stone, Shield Splitter, Doom Orb, Eye of the Storm,
    The World Stone, Avatar''s Parashu, Hydra''s Lament, Lernaean Bow, Dreamer''s
    Idol, Pendulum Blade, Nimble Ring, Daybreak Gavel, Helm of Radiance, Erosion,
    Pharaoh''s Curse, Rod of Asclepius, Eye of Providence, Shield of the Phoenix,
    Runeforged Hammer.'
  slot_scores:
    Berserker's Shield:
      total: 0.46
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.12
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.46
      efficiency: 0.55
      win: 0.38
      pick: 0.0
      fit: 0.63
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.45
      pick: 0.43
      fit: 0.31
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Breastplate of Valor
  - Nimble Ring
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Freya's Tears — physical protection
    swap_item: Freya's Tears
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Draconic Scale, Breastplate of Valor, Rod of Tahuti, Berserker''s Shield,
    Nimble Ring, Golden Blade, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire,
    Tyrfing, Riptalon, Kinetic Cuirass, Lernaean Bow, Silverbranch Bow, Toxic Blade,
    Pharaoh''s Curse, Soul Gem, Shogun''s Ofuda, Shield Splitter, Tekko-Kagi, Bragi''s
    Harp, Eye of the Storm, Hydra''s Lament, The Reaper, Daybreak Gavel, Dominance,
    Avenging Blade, Helm of Radiance, Bracer of The Abyss, Rod of Asclepius, Spear
    of the Magus, Erosion, Shield of the Phoenix, Eye of Providence, Qin''s Blade,
    Vital Amplifier, Heartseeker, Obsidian Shard, Runeforged Hammer.'
  slot_scores:
    Golden Blade:
      total: 0.45
      efficiency: 0.52
      win: 0.38
      pick: 0.0
      fit: 0.65
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.52
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.11
    Nimble Ring:
      total: 0.45
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.36
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.45
      pick: 0.43
      fit: 0.29
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Draconic Scale
  flex_slots:
  - Genji's Guard
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Draconic Scale,
    Jotunn''s Revenge, Rod of Tahuti, Berserker''s Shield, Amanita Charm, Spear of
    Desolation, Hydra''s Lament, Shield of the Phoenix, Soul Gem, Prophetic Cloak,
    Chronos'' Pendant, Kinetic Cuirass, Screeching Gargoyle, Gluttonous Grimoire,
    Arondight, Gem of Focus, Nimble Ring, Eye of Erebus, Helm of Radiance, Rod of
    Asclepius, Shield Splitter, Spear of the Magus, Chandra''s Grace, Eye of the Storm,
    Daybreak Gavel, Obsidian Shard, Erosion, Pharaoh''s Curse, Jade Scepter, Lernaean
    Bow, Eye of Providence, Wish-Granting Pearl, Avenging Blade, Totem of Death, Pendulum
    Blade, Shogun''s Ofuda, Runeforged Hammer, Gladiator''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.48
      efficiency: 0.66
      win: 0.38
      pick: 0.19
      fit: 0.44
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.12
      fit: 0.44
    Jotunn's Revenge:
      total: 0.5
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.49
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.38
      pick: 0.31
      fit: 0.52
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.45
      pick: 0.43
      fit: 0.31
    Draconic Scale:
      total: 0.53
      efficiency: 0.5
      win: 0.67
      pick: 0.11
      fit: 0.31
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
    Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Breastplate of Valor,
    Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic
    Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s
    Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian
    Mail, Triton''s Conch, Stone of Binding, Dominance, Hide of the Nemean Lion, Spear
    of the Magus, Titan''s Bane, Death Metal, Leviathan''s Hide, Jade Scepter, The
    Crusher, Void Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.48
      efficiency: 0.68
      win: 0.38
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.48
      efficiency: 0.72
      win: 0.38
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.45
      efficiency: 0.56
      win: 0.38
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.44
      efficiency: 0.55
      win: 0.38
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.38
      efficiency: 0.57
      win: 0.2
      pick: 0.07
      fit: 0.56
    Amanita Charm:
      total: 0.47
      efficiency: 0.65
      win: 0.38
      pick: 0.0
      fit: 0.45
  starter: *id001
---
