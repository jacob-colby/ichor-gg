---
type: smite-build
god: Ymir
mode: Conquest
builds:
- source: community
  aspect: null
  aspect_pick_rate: null
  aspect_win_rate: null
  slot_order:
  - name: Shifter's Shield
    pick_rate: 0.32
    win_rate: 0.75
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.24
      win_rate: 0.78
    - name: Dagger of Frenzy
      pick_rate: 0.13
      win_rate: 0.6
  - name: Stampede
    pick_rate: 0.21
    win_rate: 0.75
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.21
      win_rate: 0.63
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.4
  - name: Genji's Guard
    pick_rate: 0.16
    win_rate: 0.83
    alternates:
    - name: Kinetic Cuirass
      pick_rate: 0.16
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.6
    alternates:
    - name: Resolute Mantle
      pick_rate: 0.14
      win_rate: 0.4
    - name: Freya's Tears
      pick_rate: 0.11
      win_rate: 0.75
  - name: Spirit Robe
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Draconic Scale
      pick_rate: 0.1
      win_rate: 0.33
    - name: Sage's Ring
      pick_rate: 0.1
      win_rate: 0.33
  - name: Captain's Ring
    pick_rate: 0.14
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.14
      win_rate: 1.0
    - name: Contagion
      pick_rate: 0.07
      win_rate: 1.0
  community_starters:
  - name: Heroism
    pick_rate: 0.16
    win_rate: 0.83
  - name: Selflessness
    pick_rate: 0.16
    win_rate: 0.67
  - name: Leather Cowl
    pick_rate: 0.13
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-08-26'
  god_win_rate: 0.6842105263157895
  god_matches_won: 26
  god_matches_played: 38
  god_division: obsidian
  god_window_start: '2026-08-25'
  god_window_end: '2026-08-26'
  god_matches_analyzed: 888
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Contagion
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Amanita Charm
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Erosion, Breastplate of Valor, Eye of
    Providence, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide
    of the Nemean Lion, Leviathan''s Hide, Void Shield, Helm of Darkness, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Hussar''s Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Contagion:
      total: 0.64
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.31
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.39
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.75
      pick: 0.32
      fit: 0.72
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.72
    Stampede:
      total: 0.6
      efficiency: 0.51
      win: 0.75
      pick: 0.29
      fit: 0.46
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Contagion
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Freya's Tears
  - Stampede
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
    this god: Amanita Charm, Shield of the Phoenix, Rod of Asclepius, Rod of Tahuti,
    Erosion, Eye of Providence, Breastplate of Valor, Ethereal Staff, Phoenix Feather,
    Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen, Soul Gem, Lifebinder, Midgardian
    Mail, Stone of Binding, Helm of Radiance, Hide of the Nemean Lion, Leviathan''s
    Hide, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Contagion:
      total: 0.65
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.37
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.35
    Freya's Tears:
      total: 0.65
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.57
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.75
      pick: 0.32
      fit: 0.7
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 1.0
    Stampede:
      total: 0.6
      efficiency: 0.51
      win: 0.75
      pick: 0.29
      fit: 0.49
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Contagion
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Stampede
  flex_slots:
  - Stampede
  - Amanita Charm
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Stone of Binding — magical protection
    swap_item: Stone of Binding
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Screeching Gargoyle, Spear of Desolation, Spear of the Magus, Void Shield, Soul
    Gem, Breastplate of Valor, Obsidian Shard, Void Stone, Erosion, Eye of Providence,
    Doom Orb, Shield of the Phoenix, Helm of Radiance, The World Stone, Magi''s Cloak,
    Dreamer''s Idol, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide of
    the Nemean Lion.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.24
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.25
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.42
    Shifter's Shield:
      total: 0.62
      efficiency: 0.55
      win: 0.75
      pick: 0.32
      fit: 0.48
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Stampede:
      total: 0.58
      efficiency: 0.51
      win: 0.75
      pick: 0.29
      fit: 0.31
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Contagion
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Breastplate of Valor, Erosion,
    Helm of Radiance, Eye of Providence, Stone of Binding, Shield of the Phoenix,
    Magi''s Cloak, Soul Gem, Bragi''s Harp, Screeching Gargoyle, Daybreak Gavel, Mantle
    Of Discord, Midgardian Mail, Rod of Asclepius, Gluttonous Grimoire, Bracer of
    The Abyss, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.21
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.2
    Bracer of The Abyss:
      total: 0.49
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.31
    Bragi's Harp:
      total: 0.49
      efficiency: 0.44
      win: 0.6
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.34
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Contagion
  - Genji's Guard
  - Breastplate of Valor
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Stampede
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Rod of Tahuti, Shield of the Phoenix, Screeching Gargoyle, Chronos'' Pendant,
    Prophetic Cloak, Helm of Radiance, Erosion, Eye of Providence, Gladiator''s Shield,
    Soul Gem, Stone of Binding, Gem of Focus, Magi''s Cloak, Spear of Desolation,
    Rod of Asclepius, Eye of Erebus, Nimble Ring, Mantle Of Discord, Glorious Pridwen,
    Midgardian Mail, Daybreak Gavel, Chandra''s Grace.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.23
    Genji's Guard:
      total: 0.69
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.75
      pick: 0.32
      fit: 0.45
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.29
      fit: 0.29
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Contagion
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Shield Splitter, Runeforged Hammer, Breastplate of Valor,
    Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker,
    Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Spear of the Magus, Tekko-Kagi,
    Eye of Providence, Avenging Blade, Helm of Radiance, Stone of Binding, Shield
    of the Phoenix, Soul Gem, Titan''s Bane, Obsidian Shard, Silverbranch Bow, The
    Crusher, Pharaoh''s Curse, Magi''s Cloak, Toxic Blade, Nimble Ring, The Reaper,
    Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian Mail.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.22
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.37
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.75
      pick: 0.32
      fit: 0.42
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.29
      fit: 0.27
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Contagion
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Stampede
  flex_slots:
  - Jotunn's Revenge
  - Stampede
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Berserker''s Shield, Gluttonous Grimoire, Shield Splitter, Breastplate
    of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Obsidian Shard, Eye of the Storm, Golden Blade, Hydra''s Lament,
    Rod of Asclepius, Heartseeker, Nimble Ring, Erosion, Eye of Providence, Stone
    of Binding, Shield of the Phoenix, Jade Scepter, Doom Orb, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Tyrfing, Magi''s Cloak, Chronos'' Pendant, The World Stone,
    Bragi''s Harp, Titan''s Bane, Helm of Darkness, Ancient Signet, Lernaean Bow.'
  slot_scores:
    Contagion:
      total: 0.63
      efficiency: 0.39
      win: 1.0
      pick: 0.22
      fit: 0.22
    Genji's Guard:
      total: 0.65
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.39
    Freya's Tears:
      total: 0.62
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.36
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.75
      pick: 0.32
      fit: 0.4
    Stampede:
      total: 0.57
      efficiency: 0.51
      win: 0.75
      pick: 0.29
      fit: 0.26
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Genji's Guard
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Erosion, Breastplate of
    Valor, Eye of Providence, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Helm of Radiance, Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic
    Cloak, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Helm of Darkness,
    Ancile, Oni Hunter''s Garb, Xibalban Effigy, Hussar''s Wings, Void Stone, Spectral
    Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.67
      efficiency: 0.66
      win: 0.83
      pick: 0.25
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.5
      pick: 0.25
      fit: 0.82
    Freya's Tears:
      total: 0.66
      efficiency: 0.61
      win: 0.75
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.65
      efficiency: 0.55
      win: 0.75
      pick: 0.32
      fit: 0.72
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.72
  starter: *id001
---
