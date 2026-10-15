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
  - name: Devourer's Gauntlet
    pick_rate: 0.25
    win_rate: 0.59
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.52
    - name: Gauntlet of Thebes
      pick_rate: 0.12
      win_rate: 0.54
  - name: Stampede
    pick_rate: 0.13
    win_rate: 0.61
    alternates:
    - name: Berserker's Shield
      pick_rate: 0.12
      win_rate: 0.55
    - name: Sanguine Lash
      pick_rate: 0.09
      win_rate: 0.61
  - name: Genji's Guard
    pick_rate: 0.08
    win_rate: 0.6
    alternates:
    - name: Stampede
      pick_rate: 0.07
      win_rate: 0.55
    - name: Berserker's Shield
      pick_rate: 0.07
      win_rate: 0.68
  - name: Freya's Tears
    pick_rate: 0.1
    win_rate: 0.58
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.61
    - name: Kinetic Cuirass
      pick_rate: 0.07
      win_rate: 0.7
  - name: Shell of Rebuke
    pick_rate: 0.04
    win_rate: 0.65
    alternates:
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.67
    - name: Spirit Robe
      pick_rate: 0.04
      win_rate: 0.68
  - name: Medal of Defense
    pick_rate: 0.09
    win_rate: 0.47
    alternates:
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 0.63
    - name: Sage's Ring
      pick_rate: 0.06
      win_rate: 0.57
  community_starters:
  - name: Leather Cowl
    pick_rate: 0.25
    win_rate: 0.49
  - name: Hunter's Cowl
    pick_rate: 0.24
    win_rate: 0.64
  - name: Selflessness
    pick_rate: 0.12
    win_rate: 0.6
  source_url: https://smitebrain.com/gods/ymir/
  last_verified: '2026-10-15'
  god_win_rate: 0.5558620689655173
  god_matches_won: 403
  god_matches_played: 725
  god_division: obsidian
  god_window_start: '2026-10-06'
  god_window_end: '2026-10-15'
  god_matches_analyzed: 9899
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Amanita Charm, Shifter''s Shield, Rod of Tahuti, Genji''s
    Guard, Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance, Mantle Of Discord,
    Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide of the Nemean Lion,
    Leviathan''s Hide, Void Shield, Helm of Darkness, Ancile, Oni Hunter''s Garb,
    Xibalban Effigy, Hussar''s Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.82
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.17
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.0
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
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Genji's Guard
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
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield,
    Rod of Asclepius, Rod of Tahuti, Genji''s Guard, Erosion, Eye of Providence, Breastplate
    of Valor, Draconic Scale, Ethereal Staff, Phoenix Feather, Yogi''s Necklace, Chandra''s
    Grace, Glorious Pridwen, Soul Gem, Lifebinder, Midgardian Mail, Stone of Binding,
    Helm of Radiance, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Magi''s
    Cloak, Ancile, Oni Hunter''s Garb.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.35
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.8
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.92
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.17
      fit: 0.57
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Genji's Guard
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Void Stone — magical protection
    swap_item: Void Stone
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Kinetic Cuirass, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Screeching Gargoyle, Genji''s Guard, Spear of Desolation,
    Spear of the Magus, Void Shield, Soul Gem, Breastplate of Valor, Obsidian Shard,
    Void Stone, Shifter''s Shield, Erosion, Eye of Providence, Draconic Scale, Doom
    Orb, Shield of the Phoenix, Helm of Radiance, The World Stone, Magi''s Cloak,
    Dreamer''s Idol, Mantle Of Discord, Midgardian Mail, Rod of Asclepius, Hide of
    the Nemean Lion.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.65
    Stone of Binding:
      total: 0.56
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.25
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.58
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.17
      fit: 0.42
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Kinetic Cuirass, Rod of Tahuti, Amanita Charm, Nimble Ring, Genji''s
    Guard, Breastplate of Valor, Shifter''s Shield, Erosion, Helm of Radiance, Eye
    of Providence, Stone of Binding, Shield of the Phoenix, Draconic Scale, Magi''s
    Cloak, Soul Gem, Bragi''s Harp, Screeching Gargoyle, Daybreak Gavel, Mantle Of
    Discord, Midgardian Mail, Rod of Asclepius, Gluttonous Grimoire, Bracer of The
    Abyss, Hide of the Nemean Lion, Leviathan''s Hide, Void Shield, Ancile.'
  slot_scores:
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.2
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.48
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
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.38
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Screeching Gargoyle
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
    + fit + win/pick). Underrated for this god: Kinetic Cuirass, Genji''s Guard, Breastplate
    of Valor, Amanita Charm, Rod of Tahuti, Shield of the Phoenix, Screeching Gargoyle,
    Shifter''s Shield, Chronos'' Pendant, Prophetic Cloak, Helm of Radiance, Erosion,
    Eye of Providence, Gladiator''s Shield, Soul Gem, Draconic Scale, Stone of Binding,
    Gem of Focus, Magi''s Cloak, Spear of Desolation, Rod of Asclepius, Eye of Erebus,
    Nimble Ring, Mantle Of Discord, Glorious Pridwen, Midgardian Mail, Daybreak Gavel,
    Chandra''s Grace.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.54
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.58
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.48
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.17
      fit: 0.64
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Shield Splitter
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Kinetic Cuirass, Jotunn''s
    Revenge, Amanita Charm, Shield Splitter, Genji''s Guard, Runeforged Hammer, Breastplate
    of Valor, Golden Blade, Shifter''s Shield, Eye of the Storm, Gluttonous Grimoire,
    Hydra''s Lament, Heartseeker, Tyrfing, Lernaean Bow, Erosion, Spear of Desolation,
    Spear of the Magus, Tekko-Kagi, Eye of Providence, Avenging Blade, Helm of Radiance,
    Stone of Binding, Draconic Scale, Shield of the Phoenix, Soul Gem, Titan''s Bane,
    Obsidian Shard, Silverbranch Bow, The Crusher, Pharaoh''s Curse, Magi''s Cloak,
    Toxic Blade, Nimble Ring, The Reaper, Shogun''s Ofuda, Screeching Gargoyle, Mantle
    Of Discord, Midgardian Mail.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.55
      pick: 0.16
      fit: 0.36
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.6
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.52
    Shield Splitter:
      total: 0.54
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.17
      fit: 0.37
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Transcendence
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Kinetic Cuirass, Jotunn''s
    Revenge, Amanita Charm, Gluttonous Grimoire, Genji''s Guard, Shield Splitter,
    Breastplate of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer,
    Helm of Radiance, Soul Gem, Shifter''s Shield, Obsidian Shard, Eye of the Storm,
    Golden Blade, Hydra''s Lament, Rod of Asclepius, Heartseeker, Nimble Ring, Erosion,
    Eye of Providence, Stone of Binding, Draconic Scale, Shield of the Phoenix, Jade
    Scepter, Doom Orb, Death Metal, Wish-Granting Pearl, Avenging Blade, Tyrfing,
    Magi''s Cloak, Chronos'' Pendant, The World Stone, Bragi''s Harp, Titan''s Bane,
    Helm of Darkness, Ancient Signet, Lernaean Bow.'
  slot_scores:
    Book of Thoth:
      total: 0.47
      efficiency: 0.51
      win: 0.6
      pick: 0.0
      fit: 0.17
    Genji's Guard:
      total: 0.54
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.22
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.72
      win: 0.6
      pick: 0.0
      fit: 0.39
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.5
    Transcendence:
      total: 0.48
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.17
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
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
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Rod
    of Tahuti, Genji''s Guard, Erosion, Breastplate of Valor, Eye of Providence, Draconic
    Scale, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Helm of Radiance,
    Mantle Of Discord, Midgardian Mail, Screeching Gargoyle, Prophetic Cloak, Hide
    of the Nemean Lion, Leviathan''s Hide, Void Shield, Helm of Darkness, Ancile,
    Oni Hunter''s Garb, Xibalban Effigy, Hussar''s Wings, Void Stone, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.6
      pick: 0.12
      fit: 0.39
    Kinetic Cuirass:
      total: 0.64
      efficiency: 0.56
      win: 0.7
      pick: 0.12
      fit: 0.82
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.17
      fit: 0.64
    Shifter's Shield:
      total: 0.57
      efficiency: 0.55
      win: 0.6
      pick: 0.0
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
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
---
