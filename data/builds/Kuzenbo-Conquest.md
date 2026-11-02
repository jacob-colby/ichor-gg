---
type: smite-build
god: Kuzenbo
mode: Conquest
builds:
- source: community
  aspect: Aspect of Spirits
  aspect_pick_rate: 0.13
  aspect_win_rate: 0.44
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.3
    win_rate: 0.46
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.11
      win_rate: 0.35
    - name: Mystical Mail
      pick_rate: 0.09
      win_rate: 0.49
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.48
    alternates:
    - name: Prophetic Cloak
      pick_rate: 0.12
      win_rate: 0.56
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.51
  - name: Freya's Tears
    pick_rate: 0.14
    win_rate: 0.44
    alternates:
    - name: Genji's Guard
      pick_rate: 0.17
      win_rate: 0.45
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.46
  - name: Hide of the Nemean Lion
    pick_rate: 0.13
    win_rate: 0.43
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.52
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.47
  - name: Shell of Rebuke
    pick_rate: 0.05
    win_rate: 0.69
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.14
      win_rate: 0.6
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.4
  - name: Medal of Defense
    pick_rate: 0.1
    win_rate: 0.44
    alternates:
    - name: Olmec Blue
      pick_rate: 0.06
      win_rate: 0.27
    - name: Hide of the Nemean Lion
      pick_rate: 0.06
      win_rate: 0.44
  community_starters:
  - name: Bluestone Pendant
    pick_rate: 0.22
    win_rate: 0.37
  - name: Bluestone Brooch
    pick_rate: 0.21
    win_rate: 0.57
  - name: Selflessness
    pick_rate: 0.12
    win_rate: 0.35
  source_url: https://smitebrain.com/gods/kuzenbo/
  last_verified: '2026-11-02'
  god_win_rate: 0.4413177762525738
  god_matches_won: 643
  god_matches_played: 1457
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-11-02'
  god_matches_analyzed: 14484
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Shell of Rebuke
  - Amanita Charm
  flex_slots:
  - Prophetic Cloak
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Erosion, Breastplate
    of Valor, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone of Binding,
    Gluttonous Grimoire, Helm of Radiance, Magi''s Cloak, Shifter''s Shield, Midgardian
    Mail, Oni Hunter''s Garb, Mantle Of Discord, Leviathan''s Hide, Screeching Gargoyle,
    Void Shield, Spear of Desolation, Ancile, Rod of Asclepius, Stampede, Helm of
    Darkness, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.38
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.8
    Prophetic Cloak:
      total: 0.51
      efficiency: 0.44
      win: 0.56
      pick: 0.16
      fit: 0.62
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.62
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.69
      pick: 0.11
      fit: 0.48
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  - Shell of Rebuke
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Shield of the Phoenix
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Soul Gem, Erosion, Eye of Providence, Draconic Scale, Breastplate
    of Valor, Ethereal Staff, Gluttonous Grimoire, Phoenix Feather, Yogi''s Necklace,
    Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian Mail, Oni Hunter''s
    Garb, Shifter''s Shield, Stone of Binding, Helm of Radiance, Leviathan''s Hide,
    Void Shield, Ancile, Magi''s Cloak.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.36
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.8
    Prophetic Cloak:
      total: 0.5
      efficiency: 0.44
      win: 0.56
      pick: 0.16
      fit: 0.57
    Freya's Tears:
      total: 0.51
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.57
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.53
      win: 0.45
      pick: 0.0
      fit: 0.92
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 1.0
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Stone of Binding,
    Kinetic Cuirass, Spear of Desolation, Spear of the Magus, Screeching Gargoyle,
    Soul Gem, Void Shield, Obsidian Shard, Void Stone, Breastplate of Valor, Erosion,
    Doom Orb, Eye of Providence, Shield of the Phoenix, Draconic Scale, The World
    Stone, Helm of Radiance, Dreamer''s Idol, Magi''s Cloak, Midgardian Mail, Oni
    Hunter''s Garb, Rod of Asclepius, Mantle Of Discord, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.49
      efficiency: 0.5
      win: 0.45
      pick: 0.0
      fit: 0.73
    Genji's Guard:
      total: 0.5
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.26
    Kinetic Cuirass:
      total: 0.49
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.49
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.42
    Rod of Tahuti:
      total: 0.57
      efficiency: 0.85
      win: 0.45
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.5
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Genji's Guard
  - Bracer of The Abyss
  - Nimble Ring
  - Freya's Tears
  - Bragi's Harp
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Helm of Radiance, Erosion, Shield of
    the Phoenix, Eye of Providence, Stone of Binding, Draconic Scale, Spear of the
    Magus, Spear of Desolation, Daybreak Gavel, Bragi''s Harp, Rod of Asclepius, Magi''s
    Cloak, Midgardian Mail, Bracer of The Abyss, Screeching Gargoyle, Oni Hunter''s
    Garb, Lotus Sickle, Obsidian Shard, Mantle Of Discord, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.19
    Bracer of The Abyss:
      total: 0.42
      efficiency: 0.52
      win: 0.45
      pick: 0.0
      fit: 0.25
    Nimble Ring:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.31
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.31
    Bragi's Harp:
      total: 0.43
      efficiency: 0.44
      win: 0.45
      pick: 0.0
      fit: 0.45
    Amanita Charm:
      total: 0.48
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.35
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Breastplate of Valor,
    Amanita Charm, Shield of the Phoenix, Kinetic Cuirass, Spear of Desolation, Soul
    Gem, Lotus Sickle, Screeching Gargoyle, Chronos'' Pendant, Gluttonous Grimoire,
    Helm of Radiance, Gladiator''s Shield, Erosion, Eye of Providence, Draconic Scale,
    Gem of Focus, Stone of Binding, Eye of Erebus, Rod of Asclepius, Spear of the
    Magus, Magi''s Cloak, Midgardian Mail, Chandra''s Grace, Daybreak Gavel, Shifter''s
    Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.53
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.48
    Breastplate of Valor:
      total: 0.5
      efficiency: 0.64
      win: 0.45
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.53
    Prophetic Cloak:
      total: 0.51
      efficiency: 0.44
      win: 0.56
      pick: 0.16
      fit: 0.63
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.63
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.43
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Freya's Tears
  - Kinetic Cuirass
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Prophetic Cloak — physical protection
    swap_item: Prophetic Cloak
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged
    Hammer, Breastplate of Valor, Gluttonous Grimoire, Eye of the Storm, Hydra''s
    Lament, Tyrfing, Heartseeker, Spear of Desolation, Spear of the Magus, Lernaean
    Bow, Tekko-Kagi, Avenging Blade, Erosion, Soul Gem, Helm of Radiance, Silverbranch
    Bow, Obsidian Shard, Eye of Providence, Shield of the Phoenix, Titan''s Bane,
    The Crusher, Draconic Scale, Toxic Blade, Stone of Binding, Pharaoh''s Curse,
    Nimble Ring, The Reaper, Magi''s Cloak, Bragi''s Harp, Daybreak Gavel, Shogun''s
    Ofuda, Rod of Asclepius, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.22
    Berserker's Shield:
      total: 0.49
      efficiency: 0.68
      win: 0.45
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.47
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.35
    Kinetic Cuirass:
      total: 0.47
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.49
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Prophetic Cloak
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Prophetic Cloak
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Dreamer's Idol — CC-immunity / cleanse
    swap_item: Dreamer's Idol
  - vs_tag: magic_heavy
    swap: Shield Splitter — magical protection
    swap_item: Shield Splitter
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Gluttonous Grimoire, Kinetic Cuirass, Spear of Desolation, Spear
    of the Magus, Shield Splitter, Soul Gem, Breastplate of Valor, Runeforged Hammer,
    Helm of Radiance, Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s
    Lament, Rod of Asclepius, Lotus Sickle, Heartseeker, Erosion, Jade Scepter, Eye
    of Providence, Shield of the Phoenix, Draconic Scale, Doom Orb, Death Metal, Avenging
    Blade, Stone of Binding, Wish-Granting Pearl, The World Stone, Chronos'' Pendant,
    Titan''s Bane, The Crusher, Dreamer''s Idol, Triton''s Conch, Helm of Darkness,
    Magi''s Cloak, Daybreak Gavel, Midgardian Mail, Shifter''s Shield.'
  slot_scores:
    Genji's Guard:
      total: 0.49
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.22
    Jotunn's Revenge:
      total: 0.51
      efficiency: 0.69
      win: 0.45
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.48
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.5
    Prophetic Cloak:
      total: 0.47
      efficiency: 0.44
      win: 0.56
      pick: 0.16
      fit: 0.36
    Freya's Tears:
      total: 0.48
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.36
    Amanita Charm:
      total: 0.49
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.4
  community_ordered:
  - Genji's Guard
  - Prophetic Cloak
  - Freya's Tears
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
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Erosion, Breastplate of Valor, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Gluttonous Grimoire, Helm of Radiance, Magi''s
    Cloak, Midgardian Mail, Oni Hunter''s Garb, Mantle Of Discord, Leviathan''s Hide,
    Screeching Gargoyle, Void Shield, Spear of Desolation, Ancile, Rod of Asclepius,
    Stampede, Helm of Darkness, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.38
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.62
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.35
      pick: 0.11
      fit: 0.7
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.7
    Erosion:
      total: 0.49
      efficiency: 0.51
      win: 0.45
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Genji's Guard
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Shell of Rebuke
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Erosion — magical protection
    swap_item: Erosion
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Shifter''s Shield, Erosion, Breastplate of Valor, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Stone of Binding, Gluttonous Grimoire,
    Helm of Radiance, Magi''s Cloak, Midgardian Mail, Oni Hunter''s Garb, Mantle Of
    Discord, Leviathan''s Hide, Screeching Gargoyle, Void Shield, Spear of Desolation,
    Ancile, Rod of Asclepius, Stampede, Helm of Darkness, Spectral Armor.'
  slot_scores:
    Genji's Guard:
      total: 0.51
      efficiency: 0.66
      win: 0.48
      pick: 0.2
      fit: 0.38
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.57
      win: 0.45
      pick: 0.0
      fit: 0.8
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.69
      pick: 0.11
      fit: 0.48
    Freya's Tears:
      total: 0.52
      efficiency: 0.61
      win: 0.44
      pick: 0.22
      fit: 0.62
    Shifter's Shield:
      total: 0.46
      efficiency: 0.55
      win: 0.35
      pick: 0.11
      fit: 0.7
    Amanita Charm:
      total: 0.53
      efficiency: 0.65
      win: 0.45
      pick: 0.0
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  swaps:
  - added: Shell of Rebuke
    removed: Erosion
    reason: community 69% win over 73 matches (vs 44% on this god), taking the model's
      weakest slot from Erosion
  starter: *id001
---
