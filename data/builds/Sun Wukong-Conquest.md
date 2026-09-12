---
type: smite-build
god: Sun Wukong
mode: Conquest
builds:
- source: community
  aspect: Aspect of Transformation
  aspect_pick_rate: 0.21
  aspect_win_rate: 0.29
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.47
    win_rate: 0.53
    alternates:
    - name: Book of Thoth
      pick_rate: 0.09
      win_rate: 0.33
    - name: Devourer's Gauntlet
      pick_rate: 0.07
      win_rate: 0.8
  - name: Gladiator's Shield
    pick_rate: 0.13
    win_rate: 0.56
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.13
      win_rate: 0.67
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.33
  - name: Genji's Guard
    pick_rate: 0.18
    win_rate: 0.67
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.25
    - name: Shell of Rebuke
      pick_rate: 0.06
      win_rate: 0.5
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.5
    - name: Gladiator's Shield
      pick_rate: 0.06
      win_rate: 1.0
  - name: Brawler’s Beat Stick
    pick_rate: 0.09
    win_rate: 0.8
    alternates:
    - name: Obsidian Shard
      pick_rate: 0.07
      win_rate: 0.0
    - name: Triton's Conch
      pick_rate: 0.05
      win_rate: 0.33
  - name: Medal of Disruption
    pick_rate: 0.05
    win_rate: 0.5
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.08
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.0
  community_starters:
  - name: Bluestone Brooch
    pick_rate: 0.37
    win_rate: 0.52
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.53
  - name: Pendulum of the Ages
    pick_rate: 0.1
    win_rate: 0.43
  source_url: https://smitebrain.com/gods/sun-wukong/
  last_verified: '2026-09-12'
  god_win_rate: 0.47058823529411764
  god_matches_won: 32
  god_matches_played: 68
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-12'
  god_matches_analyzed: 4284
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Shifter's Shield
  - Berserker's Shield
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Shifter's Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Hide of the Nemean Lion — physical protection
    swap_item: Hide of the Nemean Lion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s Shield, Amanita Charm,
    Runeforged Hammer, Kinetic Cuirass, Hide of the Nemean Lion, Shield Splitter,
    Eye of the Storm, Avenging Blade, Gluttonous Grimoire, Lernaean Bow, Breastplate
    of Valor, Hydra''s Lament, Erosion, Pharaoh''s Curse, Eye of Providence, Heartseeker,
    Draconic Scale, Shogun''s Ofuda, Golden Blade, Shield of the Phoenix, Tekko-Kagi,
    Bragi''s Harp, Rod of Asclepius, Daybreak Gavel, Nimble Ring, Helm of Radiance,
    Midgardian Mail, Stone of Binding, Dominance, Spear of the Magus, Titan''s Bane,
    Death Metal, Leviathan''s Hide, Jade Scepter, The Crusher, Void Shield, Triton''s
    Conch.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.55
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.25
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.67
      pick: 0.28
      fit: 0.17
    Shifter's Shield:
      total: 0.52
      efficiency: 0.55
      win: 0.53
      pick: 0.47
      fit: 0.45
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.37
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Shifter's Shield
  - Berserker's Shield
  - Devourer's Gauntlet
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Shifter's Shield
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
    this god: Amanita Charm, Rod of Tahuti, Berserker''s Shield, Jotunn''s Revenge,
    Kinetic Cuirass, Shield of the Phoenix, Rod of Asclepius, Hide of the Nemean Lion,
    Runeforged Hammer, Shield Splitter, Eye of the Storm, Soul Gem, Erosion, Ethereal
    Staff, The Reaper, Breastplate of Valor, Eye of Providence, Yogi''s Necklace,
    Draconic Scale, Phoenix Feather, Gluttonous Grimoire, Avenging Blade, Pharaoh''s
    Curse, Shogun''s Ofuda, Lernaean Bow, Hydra''s Lament, Lifebinder, Stone of Binding,
    Midgardian Mail, Helm of Radiance, Chandra''s Grace, Daybreak Gavel, Magi''s Cloak,
    Leviathan''s Hide, Sphere of Negation, Void Shield, Stampede, Heartseeker, Ancile.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.57
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.33
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.67
      pick: 0.28
      fit: 0.2
    Shifter's Shield:
      total: 0.54
      efficiency: 0.55
      win: 0.53
      pick: 0.47
      fit: 0.54
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.48
    Devourer's Gauntlet:
      total: 0.54
      efficiency: 0.29
      win: 0.8
      pick: 0.07
      fit: 0.52
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Shifter's Shield
  - Devourer's Gauntlet
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Brawler’s Beat Stick
  - Avenging Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Gluttonous Grimoire
  flex_slots:
  - Berserker's Shield
  - Avenging Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Avatar's Parashu — CC-immunity / cleanse
    swap_item: Avatar's Parashu
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Gluttonous Grimoire, Berserker''s
    Shield, Avenging Blade, Amanita Charm, Heartseeker, Spear of the Magus, Stone
    of Binding, Spear of Desolation, Tekko-Kagi, Runeforged Hammer, Titan''s Bane,
    Kinetic Cuirass, The Crusher, Soul Gem, Void Shield, Screeching Gargoyle, The
    Reaper, Void Stone, Breastplate of Valor, Shield Splitter, Doom Orb, Eye of the
    Storm, The World Stone, Avatar''s Parashu, Hydra''s Lament, Lernaean Bow, Dreamer''s
    Idol, Pendulum Blade, Nimble Ring, Daybreak Gavel, Helm of Radiance, Erosion,
    Pharaoh''s Curse, Rod of Asclepius, Eye of Providence, Shield of the Phoenix.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.54
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.17
    Avenging Blade:
      total: 0.51
      efficiency: 0.49
      win: 0.52
      pick: 0.0
      fit: 0.72
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.67
      pick: 0.28
      fit: 0.12
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.31
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.56
    Gluttonous Grimoire:
      total: 0.52
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
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
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Nimble Ring, Golden Blade, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Tyrfing, Riptalon, Kinetic Cuirass,
    Runeforged Hammer, Lernaean Bow, Silverbranch Bow, Toxic Blade, Pharaoh''s Curse,
    Breastplate of Valor, Soul Gem, Shogun''s Ofuda, Shield Splitter, Tekko-Kagi,
    Bragi''s Harp, Eye of the Storm, Hydra''s Lament, The Reaper, Daybreak Gavel,
    Dominance, Avenging Blade, Helm of Radiance, Bracer of The Abyss, Rod of Asclepius,
    Spear of the Magus, Erosion, Shield of the Phoenix, Eye of Providence, Qin''s
    Blade, Vital Amplifier, Heartseeker, Draconic Scale.'
  slot_scores:
    Golden Blade:
      total: 0.51
      efficiency: 0.52
      win: 0.52
      pick: 0.0
      fit: 0.65
    Brawler’s Beat Stick:
      total: 0.54
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.16
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.67
      pick: 0.28
      fit: 0.11
    Berserker's Shield:
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.19
    Nimble Ring:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Brawler’s Beat Stick
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
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
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Jotunn''s Revenge, Rod of Tahuti,
    Breastplate of Valor, Berserker''s Shield, Amanita Charm, Spear of Desolation,
    Hydra''s Lament, Shield of the Phoenix, Soul Gem, Chronos'' Pendant, Kinetic Cuirass,
    Screeching Gargoyle, Gluttonous Grimoire, Runeforged Hammer, Arondight, Gem of
    Focus, Nimble Ring, Eye of Erebus, Helm of Radiance, Rod of Asclepius, Shield
    Splitter, Spear of the Magus, Prophetic Cloak, Chandra''s Grace, Eye of the Storm,
    Daybreak Gavel, Erosion, Pharaoh''s Curse, Jade Scepter, Lernaean Bow, Eye of
    Providence, Wish-Granting Pearl, Avenging Blade, Totem of Death, Draconic Scale,
    Pendulum Blade, Shogun''s Ofuda.'
  slot_scores:
    Brawler’s Beat Stick:
      total: 0.54
      efficiency: 0.42
      win: 0.8
      pick: 0.19
      fit: 0.17
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.67
      pick: 0.28
      fit: 0.44
    Berserker's Shield:
      total: 0.52
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.31
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.44
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.31
  community_ordered:
  - Brawler’s Beat Stick
  - Genji's Guard
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
      total: 0.54
      efficiency: 0.68
      win: 0.52
      pick: 0.0
      fit: 0.45
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.52
      pick: 0.0
      fit: 0.37
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.52
      pick: 0.0
      fit: 0.55
    Shield Splitter:
      total: 0.5
      efficiency: 0.55
      win: 0.52
      pick: 0.0
      fit: 0.51
    Runeforged Hammer:
      total: 0.51
      efficiency: 0.57
      win: 0.52
      pick: 0.0
      fit: 0.56
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.52
      pick: 0.0
      fit: 0.45
  starter: *id001
---
