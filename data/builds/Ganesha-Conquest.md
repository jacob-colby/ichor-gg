---
type: smite-build
god: Ganesha
mode: Conquest
builds:
- source: community
  aspect: Aspect of the Triumphant
  aspect_pick_rate: 0.14
  aspect_win_rate: 0.37
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.54
    win_rate: 0.58
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.52
    - name: Amanita Charm
      pick_rate: 0.03
      win_rate: 0.6
  - name: Stampede
    pick_rate: 0.3
    win_rate: 0.59
    alternates:
    - name: Genji's Guard
      pick_rate: 0.15
      win_rate: 0.61
    - name: Freya's Tears
      pick_rate: 0.07
      win_rate: 0.52
  - name: Genji's Guard
    pick_rate: 0.13
    win_rate: 0.55
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.57
    - name: Shell of Rebuke
      pick_rate: 0.11
      win_rate: 0.58
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.58
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.15
      win_rate: 0.61
    - name: Genji's Guard
      pick_rate: 0.06
      win_rate: 0.61
  - name: Shell of Rebuke
    pick_rate: 0.08
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.1
      win_rate: 0.72
    - name: Genji's Guard
      pick_rate: 0.04
      win_rate: 0.7
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.54
    alternates:
    - name: Sage's Ring
      pick_rate: 0.07
      win_rate: 0.45
    - name: Flaming Pearl
      pick_rate: 0.06
      win_rate: 0.78
  community_starters:
  - name: Selflessness
    pick_rate: 0.39
    win_rate: 0.55
  - name: Heroism
    pick_rate: 0.31
    win_rate: 0.64
  - name: Conduit Gem
    pick_rate: 0.09
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/ganesha/
  last_verified: '2026-10-30'
  god_win_rate: 0.5443425076452599
  god_matches_won: 178
  god_matches_played: 327
  god_division: obsidian
  god_window_start: '2026-10-20'
  god_window_end: '2026-10-30'
  god_matches_analyzed: 10706
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s Shield, Breastplate
    of Valor, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Stone
    of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of Radiance, Mantle Of Discord,
    Midgardian Mail, Oni Hunter''s Garb, Screeching Gargoyle, Prophetic Cloak, Leviathan''s
    Hide, Hide of the Nemean Lion, Void Shield, Helm of Darkness, Spear of Desolation,
    Ancile, Gladiator''s Shield, Spectral Armor.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.65
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Amanita Charm
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Shifter's Shield
  - Erosion
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Shifter''s Shield, Soul Gem, Erosion, Breastplate of Valor,
    Eye of Providence, Draconic Scale, Ethereal Staff, Gluttonous Grimoire, Phoenix
    Feather, Yogi''s Necklace, Chandra''s Grace, Glorious Pridwen, Lifebinder, Midgardian
    Mail, Oni Hunter''s Garb, Helm of Radiance, Stone of Binding, Leviathan''s Hide,
    Hide of the Nemean Lion, Void Shield, Ancile, Spear of Desolation.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.78
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.58
      pick: 0.0
      fit: 0.93
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.58
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.68
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.98
    Erosion:
      total: 0.54
      efficiency: 0.51
      win: 0.58
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Screeching Gargoyle — magical protection
    swap_item: Screeching Gargoyle
  - vs_tag: physical_heavy
    swap: Void Shield — physical protection
    swap_item: Void Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Amanita Charm, Gluttonous Grimoire, Stone of Binding,
    Kinetic Cuirass, Spear of Desolation, Screeching Gargoyle, Spear of the Magus,
    Soul Gem, Void Shield, Obsidian Shard, Breastplate of Valor, Void Stone, Shifter''s
    Shield, Erosion, Eye of Providence, Draconic Scale, Shield of the Phoenix, Doom
    Orb, Helm of Radiance, The World Stone, Dreamer''s Idol, Magi''s Cloak, Midgardian
    Mail, Mantle Of Discord, Oni Hunter''s Garb, Rod of Asclepius.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.75
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.59
    Freya's Tears:
      total: 0.56
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.45
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.51
    Rod of Tahuti:
      total: 0.62
      efficiency: 0.85
      win: 0.58
      pick: 0.0
      fit: 0.41
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.49
  community_ordered:
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Bragi's Harp
  - Bracer of The Abyss
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Amanita Charm, Nimble Ring, Kinetic Cuirass, Gluttonous
    Grimoire, Breastplate of Valor, Soul Gem, Shifter''s Shield, Helm of Radiance,
    Erosion, Shield of the Phoenix, Eye of Providence, Stone of Binding, Draconic
    Scale, Spear of Desolation, Magi''s Cloak, Spear of the Magus, Daybreak Gavel,
    Screeching Gargoyle, Bragi''s Harp, Rod of Asclepius, Midgardian Mail, Oni Hunter''s
    Garb, Lotus Sickle, Mantle Of Discord, Bracer of The Abyss, Obsidian Shard.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.46
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.24
    Nimble Ring:
      total: 0.53
      efficiency: 0.65
      win: 0.58
      pick: 0.0
      fit: 0.3
    Bragi's Harp:
      total: 0.48
      efficiency: 0.44
      win: 0.58
      pick: 0.0
      fit: 0.44
    Freya's Tears:
      total: 0.54
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.33
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.36
  community_ordered:
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
  - Spear of Desolation
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Amanita Charm, Breastplate
    of Valor, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Soul Gem,
    Lotus Sickle, Screeching Gargoyle, Shifter''s Shield, Chronos'' Pendant, Prophetic
    Cloak, Helm of Radiance, Erosion, Gluttonous Grimoire, Eye of Providence, Gladiator''s
    Shield, Draconic Scale, Stone of Binding, Gem of Focus, Magi''s Cloak, Spear of
    the Magus, Rod of Asclepius, Eye of Erebus, Midgardian Mail, Mantle Of Discord,
    Oni Hunter''s Garb.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.56
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.48
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.55
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.64
    Spear of Desolation:
      total: 0.53
      efficiency: 0.58
      win: 0.58
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Amanita Charm
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
  - Kinetic Cuirass
  - Shield Splitter
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
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita
    Charm, Berserker''s Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged
    Hammer, Breastplate of Valor, Gluttonous Grimoire, Shifter''s Shield, Eye of the
    Storm, Hydra''s Lament, Tyrfing, Spear of Desolation, Heartseeker, Spear of the
    Magus, Erosion, Lernaean Bow, Eye of Providence, Soul Gem, Helm of Radiance, Tekko-Kagi,
    Shield of the Phoenix, Avenging Blade, Draconic Scale, Silverbranch Bow, Obsidian
    Shard, Stone of Binding, Titan''s Bane, The Crusher, Toxic Blade, Pharaoh''s Curse,
    Nimble Ring, Magi''s Cloak, The Reaper, Screeching Gargoyle, Midgardian Mail,
    Shogun''s Ofuda, Daybreak Gavel.'
  slot_scores:
    Berserker's Shield:
      total: 0.55
      efficiency: 0.68
      win: 0.58
      pick: 0.0
      fit: 0.35
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.54
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.51
    Shield Splitter:
      total: 0.53
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.51
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.38
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.41
  community_ordered:
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Jotunn's Revenge
  - Transcendence
  - Freya's Tears
  - Rod of Tahuti
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Shield Splitter — physical protection
    swap_item: Shield Splitter
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Spear of Desolation, Shield
    Splitter, Spear of the Magus, Breastplate of Valor, Soul Gem, Helm of Radiance,
    Runeforged Hammer, Obsidian Shard, Shifter''s Shield, Berserker''s Shield, Eye
    of the Storm, Hydra''s Lament, Rod of Asclepius, Erosion, Lotus Sickle, Eye of
    Providence, Shield of the Phoenix, Heartseeker, Draconic Scale, Jade Scepter,
    Stone of Binding, Doom Orb, Death Metal, Avenging Blade, Chronos'' Pendant, Wish-Granting
    Pearl, The World Stone, Magi''s Cloak, Helm of Darkness, Titan''s Bane, The Crusher,
    Dreamer''s Idol, Screeching Gargoyle, Midgardian Mail, Triton''s Conch.'
  slot_scores:
    Book of Thoth:
      total: 0.46
      efficiency: 0.5
      win: 0.58
      pick: 0.0
      fit: 0.18
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.69
      win: 0.58
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.47
      efficiency: 0.52
      win: 0.58
      pick: 0.0
      fit: 0.18
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.38
    Rod of Tahuti:
      total: 0.61
      efficiency: 0.85
      win: 0.58
      pick: 0.0
      fit: 0.32
    Amanita Charm:
      total: 0.56
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.41
  community_ordered:
  - Freya's Tears
  - Amanita Charm
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Genji's Guard
  - Breastplate of Valor
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Breastplate of Valor, Erosion, Eye of Providence, Draconic Scale, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Gluttonous Grimoire, Helm of
    Radiance, Mantle Of Discord, Midgardian Mail, Oni Hunter''s Garb, Screeching Gargoyle,
    Prophetic Cloak, Leviathan''s Hide, Hide of the Nemean Lion, Void Shield, Helm
    of Darkness, Spear of Desolation, Ancile, Gladiator''s Shield, Spectral Armor.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.58
      pick: 0.0
      fit: 0.4
    Genji's Guard:
      total: 0.55
      efficiency: 0.66
      win: 0.55
      pick: 0.2
      fit: 0.4
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.57
      win: 0.58
      pick: 0.0
      fit: 0.8
    Freya's Tears:
      total: 0.59
      efficiency: 0.61
      win: 0.58
      pick: 0.3
      fit: 0.65
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.58
      pick: 0.0
      fit: 0.7
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.03
      fit: 0.7
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Amanita Charm
  starter: *id001
---
