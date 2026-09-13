---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.22
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.53
    win_rate: 0.54
    alternates:
    - name: Book of Thoth
      pick_rate: 0.08
      win_rate: 0.29
    - name: Devourer's Gauntlet
      pick_rate: 0.07
      win_rate: 0.83
  - name: Gladiator's Shield
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.11
      win_rate: 0.3
    - name: Shifter's Shield
      pick_rate: 0.1
      win_rate: 0.67
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.64
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.31
    - name: Gladiator's Shield
      pick_rate: 0.09
      win_rate: 0.75
  - name: Freya's Tears
    pick_rate: 0.07
    win_rate: 0.83
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.55
    - name: Hide of the Nemean Lion
      pick_rate: 0.07
      win_rate: 0.5
  - name: Brawler’s Beat Stick
    pick_rate: 0.09
    win_rate: 0.83
    alternates:
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.25
    - name: Obsidian Shard
      pick_rate: 0.06
      win_rate: 0.0
  - name: Medal of Defense
    pick_rate: 0.08
    win_rate: 0.75
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.0
    - name: Freya's Tears
      pick_rate: 0.06
      win_rate: 0.67
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.38
    win_rate: 0.55
  - name: Bluestone Pendant
    pick_rate: 0.24
    win_rate: 0.57
  - name: Conduit Gem
    pick_rate: 0.09
    win_rate: 0.38
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-09-13'
  god_win_rate: 0.4827586206896552
  god_matches_won: 42
  god_matches_played: 87
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-13'
  god_matches_analyzed: 5560
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Breastplate of Valor,
    Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker, Draconic
    Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi, Bragi''s
    Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance, Midgardian
    Mail, Triton''s Conch, Stone of Binding, Dominance, Spear of the Magus, Titan''s
    Bane, Death Metal, Leviathan''s Hide, Jade Scepter, The Crusher, Void Shield,
    Hide of the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.83
      pick: 0.19
      fit: 0.25
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.25
      fit: 0.17
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
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.83
      pick: 0.12
      fit: 0.29
    Amanita Charm:
      total: 0.54
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Devourer's Gauntlet
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Devourer's Gauntlet
  - Berserker's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s
    Revenge, Kinetic Cuirass, Shield of the Phoenix, Rod of Asclepius, Runeforged
    Hammer, Shield Splitter, Eye of the Storm, Soul Gem, Erosion, Ethereal Staff,
    The Reaper, Breastplate of Valor, Eye of Providence, Yogi''s Necklace, Draconic
    Scale, Phoenix Feather, Gluttonous Grimoire, Avenging Blade, Pharaoh''s Curse,
    Shogun''s Ofuda, Lernaean Bow, Hydra''s Lament, Lifebinder, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Chandra''s Grace, Daybreak Gavel, Magi''s Cloak,
    Leviathan''s Hide, Sphere of Negation, Void Shield, Stampede, Heartseeker, Ancile,
    Hide of the Nemean Lion.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.58
      efficiency: 0.42
      win: 0.83
      pick: 0.19
      fit: 0.33
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.64
      pick: 0.25
      fit: 0.2
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.48
    Devourer's Gauntlet:
      total: 0.56
      efficiency: 0.29
      win: 0.83
      pick: 0.07
      fit: 0.52
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.83
      pick: 0.12
      fit: 0.37
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Devourer's Gauntlet
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Gluttonous Grimoire
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
    for this god: Freya''s Tears, Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire,
    Berserker''s Shield, Avenging Blade, Amanita Charm, Heartseeker, Spear of the
    Magus, Stone of Binding, Spear of Desolation, Tekko-Kagi, Runeforged Hammer, Titan''s
    Bane, Kinetic Cuirass, The Crusher, Soul Gem, Void Shield, Screeching Gargoyle,
    The Reaper, Void Stone, Breastplate of Valor, Shield Splitter, Doom Orb, Eye of
    the Storm, The World Stone, Avatar''s Parashu, Hydra''s Lament, Lernaean Bow,
    Dreamer''s Idol, Pendulum Blade, Nimble Ring, Daybreak Gavel, Helm of Radiance,
    Erosion, Pharaoh''s Curse, Rod of Asclepius, Eye of Providence, Shield of the
    Phoenix, Obsidian Shard.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.56
      efficiency: 0.42
      win: 0.83
      pick: 0.19
      fit: 0.17
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.64
      pick: 0.25
      fit: 0.12
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
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.83
      pick: 0.12
      fit: 0.2
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.55
      win: 0.55
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Freya's Tears
  - Nimble Ring
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Rod of Tahuti, Berserker''s Shield, Nimble Ring, Golden
    Blade, Jotunn''s Revenge, Amanita Charm, Gluttonous Grimoire, Tyrfing, Riptalon,
    Kinetic Cuirass, Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Toxic Blade,
    Pharaoh''s Curse, Breastplate of Valor, Soul Gem, Shogun''s Ofuda, Shield Splitter,
    Tekko-Kagi, Bragi''s Harp, Eye of the Storm, Hydra''s Lament, The Reaper, Daybreak
    Gavel, Dominance, Avenging Blade, Helm of Radiance, Bracer of The Abyss, Rod of
    Asclepius, Spear of the Magus, Erosion, Shield of the Phoenix, Eye of Providence,
    Qin''s Blade, Vital Amplifier, Heartseeker, Draconic Scale, Obsidian Shard.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.55
      pick: 0.0
      fit: 0.65
    Brawler’s Beat Stick:
      total: 0.55
      efficiency: 0.42
      win: 0.83
      pick: 0.19
      fit: 0.16
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.64
      pick: 0.25
      fit: 0.11
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.83
      pick: 0.12
      fit: 0.19
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.55
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - Jotunn's Revenge
  flex_slots:
  - Breastplate of Valor
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
    + fit + win/pick). Underrated for this god: Freya''s Tears, Jotunn''s Revenge,
    Rod of Tahuti, Breastplate of Valor, Berserker''s Shield, Amanita Charm, Spear
    of Desolation, Hydra''s Lament, Shield of the Phoenix, Soul Gem, Chronos'' Pendant,
    Kinetic Cuirass, Screeching Gargoyle, Gluttonous Grimoire, Runeforged Hammer,
    Arondight, Gem of Focus, Nimble Ring, Eye of Erebus, Helm of Radiance, Rod of
    Asclepius, Shield Splitter, Spear of the Magus, Chandra''s Grace, Eye of the Storm,
    Daybreak Gavel, Erosion, Pharaoh''s Curse, Jade Scepter, Lernaean Bow, Eye of
    Providence, Wish-Granting Pearl, Avenging Blade, Totem of Death, Draconic Scale,
    Pendulum Blade, Shogun''s Ofuda, Obsidian Shard.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.56
      efficiency: 0.42
      win: 0.83
      pick: 0.19
      fit: 0.17
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.64
      pick: 0.25
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
    Freya's Tears:
      total: 0.67
      efficiency: 0.61
      win: 0.83
      pick: 0.12
      fit: 0.52
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.55
      pick: 0.0
      fit: 0.49
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
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
    Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield,
    Amanita Charm, Runeforged Hammer, Kinetic Cuirass, Shield Splitter, Eye of the
    Storm, Freya''s Tears, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Breastplate
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
      total: 0.52
      efficiency: 0.56
      win: 0.55
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.51
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
