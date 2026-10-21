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
  - name: Gauntlet of Thebes
    pick_rate: 0.26
    win_rate: 0.72
    alternates:
    - name: Devourer's Gauntlet
      pick_rate: 0.15
      win_rate: 0.4
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.71
  - name: Berserker's Shield
    pick_rate: 0.18
    win_rate: 0.42
    alternates:
    - name: Stampede
      pick_rate: 0.18
      win_rate: 0.5
    - name: Shifter's Shield
      pick_rate: 0.12
      win_rate: 0.5
  - name: Shell of Rebuke
    pick_rate: 0.14
    win_rate: 0.78
    alternates:
    - name: Sanguine Lash
      pick_rate: 0.06
      win_rate: 0.25
    - name: Shogun's Ofuda
      pick_rate: 0.06
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.11
    win_rate: 0.43
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.6
    - name: Shogun's Ofuda
      pick_rate: 0.08
      win_rate: 0.2
  - name: Hussar's Wings
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.75
    - name: Mana Tome
      pick_rate: 0.06
      win_rate: 1.0
  - name: Hide of the Nemean Lion
    pick_rate: 0.1
    win_rate: 0.67
    alternates:
    - name: Medallion
      pick_rate: 0.06
      win_rate: 0.5
    - name: Medal of Disruption
      pick_rate: 0.06
      win_rate: 0.5
  community_starters:
  - name: Leather Cowl
    pick_rate: 0.25
    win_rate: 0.41
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.44
  - name: Warrior's Axe
    pick_rate: 0.16
    win_rate: 0.55
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-10-21'
  god_win_rate: 0.5441176470588235
  god_matches_won: 37
  god_matches_played: 68
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-21'
  god_matches_analyzed: 814
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Kinetic Cuirass
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s Guard, Erosion,
    Breastplate of Valor, Eye of Providence, Draconic Scale, Shield of the Phoenix,
    Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide, Void Shield, Helm
    of Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Void Stone, Spectral
    Armor.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.82
    Shell of Rebuke:
      total: 0.54
      efficiency: 0.28
      win: 0.78
      pick: 0.22
      fit: 0.51
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.46
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.43
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.16
      fit: 0.72
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - Freya's Tears
  - Shifter's Shield
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Eye of Providence — physical protection
    swap_item: Eye of Providence
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Rod of Asclepius,
    Rod of Tahuti, Erosion, Eye of Providence, Genji''s Guard, Breastplate of Valor,
    Draconic Scale, Ethereal Staff, Phoenix Feather, Yogi''s Necklace, Chandra''s
    Grace, Glorious Pridwen, Soul Gem, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s
    Garb.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.8
    Shield of the Phoenix:
      total: 0.55
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.92
    Shell of Rebuke:
      total: 0.53
      efficiency: 0.28
      win: 0.78
      pick: 0.22
      fit: 0.43
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.16
      fit: 0.7
    Hide of the Nemean Lion:
      total: 0.57
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.49
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Shell of Rebuke
  - Shifter's Shield
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Kinetic Cuirass
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Stone of Binding, Gluttonous Grimoire,
    Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation, Spear of the Magus,
    Void Shield, Soul Gem, Genji''s Guard, Breastplate of Valor, Obsidian Shard, Void
    Stone, Erosion, Eye of Providence, Draconic Scale, Doom Orb, Shield of the Phoenix,
    Helm of Radiance, The World Stone, Magi''s Cloak, Dreamer''s Idol, Mantle Of Discord,
    Midgardian Mail, Rod of Asclepius.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.5
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.74
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.58
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.28
      win: 0.78
      pick: 0.22
      fit: 0.34
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.31
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Shell of Rebuke
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Bracer of The Abyss
  - Nimble Ring
  - Shell of Rebuke
  - Bragi's Harp
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Genji''s
    Guard, Breastplate of Valor, Erosion, Helm of Radiance, Eye of Providence, Stone
    of Binding, Shield of the Phoenix, Draconic Scale, Magi''s Cloak, Soul Gem, Bragi''s
    Harp, Screeching Gargoyle, Daybreak Gavel, Mantle Of Discord, Midgardian Mail,
    Rod of Asclepius, Gluttonous Grimoire, Bracer of The Abyss, Leviathan''s Hide,
    Void Shield, Ancile.'
  slot_scores:
    Bracer of The Abyss:
      total: 0.44
      efficiency: 0.52
      win: 0.5
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.5
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.31
    Shell of Rebuke:
      total: 0.5
      efficiency: 0.28
      win: 0.78
      pick: 0.22
      fit: 0.27
    Bragi's Harp:
      total: 0.45
      efficiency: 0.44
      win: 0.5
      pick: 0.0
      fit: 0.45
    Hide of the Nemean Lion:
      total: 0.53
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.24
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Shell of Rebuke
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Shell of Rebuke
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
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Genji''s Guard, Breastplate of Valor,
    Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Screeching
    Gargoyle, Chronos'' Pendant, Prophetic Cloak, Helm of Radiance, Erosion, Eye of
    Providence, Gladiator''s Shield, Soul Gem, Draconic Scale, Stone of Binding, Gem
    of Focus, Magi''s Cloak, Spear of Desolation, Rod of Asclepius, Eye of Erebus,
    Nimble Ring, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Chandra''s Grace.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.48
    Breastplate of Valor:
      total: 0.53
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.48
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.28
      win: 0.78
      pick: 0.22
      fit: 0.32
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.29
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.43
      pick: 0.18
      fit: 0.64
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Shield Splitter
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Genji''s Guard, Breastplate
    of Valor, Golden Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament,
    Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation, Spear of the
    Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance, Stone
    of Binding, Draconic Scale, Shield of the Phoenix, Soul Gem, Titan''s Bane, Obsidian
    Shard, Silverbranch Bow, The Crusher, Pharaoh''s Curse, Magi''s Cloak, Toxic Blade,
    Nimble Ring, The Reaper, Screeching Gargoyle, Mantle Of Discord, Midgardian Mail,
    Shogun''s Ofuda.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.54
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shield Splitter:
      total: 0.49
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.52
    Shell of Rebuke:
      total: 0.51
      efficiency: 0.28
      win: 0.78
      pick: 0.22
      fit: 0.3
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.27
    Amanita Charm:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Shell of Rebuke
  - Hide of the Nemean Lion
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shell of Rebuke
  - Hide of the Nemean Lion
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Genji''s Guard, Shield Splitter,
    Breastplate of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer,
    Helm of Radiance, Soul Gem, Obsidian Shard, Eye of the Storm, Golden Blade, Hydra''s
    Lament, Rod of Asclepius, Heartseeker, Nimble Ring, Erosion, Eye of Providence,
    Stone of Binding, Draconic Scale, Shield of the Phoenix, Jade Scepter, Doom Orb,
    Death Metal, Wish-Granting Pearl, Avenging Blade, Tyrfing, Magi''s Cloak, Chronos''
    Pendant, The World Stone, Bragi''s Harp, Titan''s Bane, Helm of Darkness, Ancient
    Signet, Lernaean Bow.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.22
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.72
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.5
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.5
    Shell of Rebuke:
      total: 0.5
      efficiency: 0.28
      win: 0.78
      pick: 0.22
      fit: 0.29
    Hide of the Nemean Lion:
      total: 0.54
      efficiency: 0.52
      win: 0.67
      pick: 0.31
      fit: 0.26
    Amanita Charm:
      total: 0.51
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Shell of Rebuke
  - Hide of the Nemean Lion
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Rod of Tahuti, Genji''s
    Guard, Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide, Void
    Shield, Helm of Darkness, Ancile, Oni Hunter''s Garb, Xibalban Effigy, Void Stone,
    Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.5
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.56
      win: 0.5
      pick: 0.0
      fit: 0.82
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.43
      pick: 0.18
      fit: 0.64
    Shifter's Shield:
      total: 0.53
      efficiency: 0.55
      win: 0.5
      pick: 0.16
      fit: 0.72
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.72
    Erosion:
      total: 0.51
      efficiency: 0.51
      win: 0.5
      pick: 0.0
      fit: 0.72
  community_ordered:
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
