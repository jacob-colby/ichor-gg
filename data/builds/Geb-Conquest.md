---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.01
  aspect_win_rate: 1.0
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.2
    win_rate: 0.53
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.69
    - name: Chronos' Pendant
      pick_rate: 0.16
      win_rate: 0.48
  - name: Genji's Guard
    pick_rate: 0.3
    win_rate: 0.65
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.18
      win_rate: 0.61
    - name: Stampede
      pick_rate: 0.09
      win_rate: 0.33
  - name: Breastplate of Valor
    pick_rate: 0.19
    win_rate: 0.69
    alternates:
    - name: Genji's Guard
      pick_rate: 0.22
      win_rate: 0.59
    - name: Ragnarok's Wake
      pick_rate: 0.09
      win_rate: 0.6
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.74
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.59
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.5
  - name: Glorious Pridwen
    pick_rate: 0.08
    win_rate: 0.58
    alternates:
    - name: Spirit Robe
      pick_rate: 0.08
      win_rate: 0.67
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.45
  - name: Engraved Guard
    pick_rate: 0.12
    win_rate: 0.7
    alternates:
    - name: Olmec Blue
      pick_rate: 0.07
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 1.0
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-08-01'
  god_win_rate: 0.5755813953488372
  god_matches_won: 99
  god_matches_played: 172
  god_division: obsidian
  god_window_start: '2026-07-28'
  god_window_end: '2026-08-01'
  god_matches_analyzed: 4952
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Eye of Providence, Shifter''s
    Shield, Erosion, Oni Hunter''s Garb, Draconic Scale, Shield of the Phoenix, Spectral
    Armor, Gluttonous Grimoire, Leviathan''s Hide, Stone of Binding, Mantle Of Discord,
    Midgardian Mail, Hide of the Nemean Lion, Magi''s Cloak, Gladiator''s Shield,
    Hussar''s Wings, Prophetic Cloak, Ancile, Yogi''s Necklace, Void Shield, Xibalban
    Effigy.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.45
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.69
      pick: 0.19
      fit: 0.45
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.66
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.76
    Amanita Charm:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.85
    Stampede:
      total: 0.59
      efficiency: 0.53
      win: 0.69
      pick: 0.19
      fit: 0.55
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Stampede
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Hussar's Wings — CC-immunity / cleanse
    swap_item: Hussar's Wings
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Shield of the Phoenix,
    Eye of Providence, Shifter''s Shield, Glorious Pridwen, Oni Hunter''s Garb, Erosion,
    Chandra''s Grace, Draconic Scale, Rod of Asclepius, Phoenix Feather, Spectral
    Armor, Gluttonous Grimoire, Soul Gem, Leviathan''s Hide, Midgardian Mail, Hide
    of the Nemean Lion, Gladiator''s Shield, Yogi''s Necklace, Ancile, Lifebinder,
    Void Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.62
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.42
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.19
      fit: 0.42
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.94
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.68
    Amanita Charm:
      total: 0.61
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.59
      efficiency: 0.53
      win: 0.69
      pick: 0.19
      fit: 0.58
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - Stampede
  flex_slots:
  - Gluttonous Grimoire
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Freya''s Tears, Gluttonous Grimoire, Amanita Charm, Kinetic Cuirass,
    Eye of Providence, Soul Gem, Stone of Binding, Oni Hunter''s Garb, Void Shield,
    Screeching Gargoyle, Shifter''s Shield, Spear of the Magus, Void Stone, Shield
    of the Phoenix, Erosion, The Cosmic Horror, Spectral Armor, Draconic Scale, Spear
    of Desolation, Yogi''s Necklace, Obsidian Shard, Leviathan''s Hide, Midgardian
    Mail, Mantle Of Discord, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.28
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.65
      win: 0.69
      pick: 0.19
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.63
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.47
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.63
    Stampede:
      total: 0.56
      efficiency: 0.53
      win: 0.69
      pick: 0.19
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Amanita Charm, Kinetic Cuirass, Eye of Providence, Gluttonous
    Grimoire, Oni Hunter''s Garb, Shifter''s Shield, Shield of the Phoenix, Spectral
    Armor, Erosion, Yogi''s Necklace, Soul Gem, Draconic Scale, Leviathan''s Hide,
    Midgardian Mail, Bracer of The Abyss, Bragi''s Harp, Hide of the Nemean Lion,
    Stone of Binding, Helm of Radiance, Death Metal, Rod of Asclepius, Mantle Of Discord,
    Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.21
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.19
      fit: 0.21
    Bracer of The Abyss:
      total: 0.46
      efficiency: 0.57
      win: 0.5
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.44
      efficiency: 0.49
      win: 0.5
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.45
      efficiency: 0.47
      win: 0.5
      pick: 0.0
      fit: 0.42
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.35
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Stampede
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Amanita Charm, Kinetic
    Cuirass, Shield of the Phoenix, Eye of Providence, Soul Gem, Gluttonous Grimoire,
    Oni Hunter''s Garb, Shifter''s Shield, Screeching Gargoyle, Gladiator''s Shield,
    Chandra''s Grace, Erosion, Spectral Armor, Prophetic Cloak, Spear of Desolation,
    Draconic Scale, Yogi''s Necklace, Helm of Radiance, Rod of Asclepius, Gem of Focus,
    Leviathan''s Hide, Death Metal, Midgardian Mail.'
  slot_scores:
    Genji's Guard:
      total: 0.63
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.5
    Breastplate of Valor:
      total: 0.62
      efficiency: 0.65
      win: 0.69
      pick: 0.19
      fit: 0.5
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.65
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.67
    Amanita Charm:
      total: 0.53
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.47
    Stampede:
      total: 0.55
      efficiency: 0.53
      win: 0.69
      pick: 0.19
      fit: 0.3
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Breastplate of Valor
  - Freya's Tears
  - The Crusher
  - Stampede
  flex_slots:
  - Berserker's Shield
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Freya''s Tears, Berserker''s Shield, The Crusher,
    Jotunn''s Revenge, Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Eye of
    Providence, Runeforged Hammer, Hydra''s Lament, Shield Splitter, Oni Hunter''s
    Garb, Golden Blade, Eye of the Storm, Lernaean Bow, Shifter''s Shield, Pharaoh''s
    Curse, Soul Gem, Shield of the Phoenix, Avenging Blade, Erosion, Spectral Armor,
    The Reaper, Death Metal, Yogi''s Necklace, Draconic Scale, Damaru, Shogun''s Ofuda,
    Leviathan''s Hide, Tekko-Kagi, Dominance, Spear of the Magus, Heartseeker, Midgardian
    Mail, Tyrfing, Riptalon, Stone of Binding, Hide of the Nemean Lion.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.23
    Berserker's Shield:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.38
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.19
      fit: 0.23
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.39
    The Crusher:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.49
    Stampede:
      total: 0.55
      efficiency: 0.53
      win: 0.69
      pick: 0.19
      fit: 0.28
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  - Stampede
  flex_slots:
  - Gluttonous Grimoire
  - The Crusher
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Kinetic Cuirass — physical protection
    swap_item: Kinetic Cuirass
  - vs_tag: sustain
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Gluttonous Grimoire,
    Amanita Charm, The Crusher, Kinetic Cuirass, Jotunn''s Revenge, Berserker''s Shield,
    Soul Gem, Eye of Providence, Runeforged Hammer, Oni Hunter''s Garb, Hydra''s Lament,
    Death Metal, Spear of the Magus, Shield Splitter, Shifter''s Shield, The Cosmic
    Horror, Helm of Radiance, Rod of Asclepius, Eye of the Storm, Shield of the Phoenix,
    Spectral Armor, Erosion, Spear of Desolation, Jade Scepter, Yogi''s Necklace,
    Pharaoh''s Curse, Avenging Blade, Draconic Scale, Golden Blade, Obsidian Shard,
    Triton''s Conch, The Reaper, Lernaean Bow, Leviathan''s Hide, Damaru, Ethereal
    Staff.'
  slot_scores:
    Genji's Guard:
      total: 0.59
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.22
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.19
      fit: 0.22
    Freya's Tears:
      total: 0.6
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.37
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.55
    The Crusher:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.43
    Stampede:
      total: 0.55
      efficiency: 0.53
      win: 0.69
      pick: 0.19
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Eye of Providence, Shifter''s
    Shield, Freya''s Tears, Erosion, Oni Hunter''s Garb, Draconic Scale, Shield of
    the Phoenix, Spectral Armor, Gluttonous Grimoire, Leviathan''s Hide, Stone of
    Binding, Mantle Of Discord, Midgardian Mail, Hide of the Nemean Lion, Magi''s
    Cloak, Gladiator''s Shield, Hussar''s Wings, Prophetic Cloak, Ancile, Yogi''s
    Necklace, Void Shield, Xibalban Effigy.'
  slot_scores:
    Eye of Providence:
      total: 0.57
      efficiency: 0.63
      win: 0.5
      pick: 0.0
      fit: 0.85
    Genji's Guard:
      total: 0.63
      efficiency: 0.72
      win: 0.65
      pick: 0.3
      fit: 0.45
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.66
      efficiency: 0.59
      win: 0.74
      pick: 0.14
      fit: 0.76
    Shifter's Shield:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.59
      efficiency: 0.67
      win: 0.5
      pick: 0.0
      fit: 0.85
  starter: *id001
---
