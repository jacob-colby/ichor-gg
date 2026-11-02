---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.29
  aspect_win_rate: 0.49
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.27
    win_rate: 0.63
    alternates:
    - name: Stampede
      pick_rate: 0.15
      win_rate: 0.47
    - name: Mystical Mail
      pick_rate: 0.13
      win_rate: 0.55
  - name: Stampede
    pick_rate: 0.17
    win_rate: 0.56
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.66
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.61
  - name: Freya's Tears
    pick_rate: 0.15
    win_rate: 0.58
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.56
    - name: Genji's Guard
      pick_rate: 0.12
      win_rate: 0.58
  - name: Shell of Rebuke
    pick_rate: 0.13
    win_rate: 0.68
    alternates:
    - name: Freya's Tears
      pick_rate: 0.15
      win_rate: 0.51
    - name: Genji's Guard
      pick_rate: 0.1
      win_rate: 0.63
  - name: Kinetic Cuirass
    pick_rate: 0.05
    win_rate: 0.42
    alternates:
    - name: Freya's Tears
      pick_rate: 0.09
      win_rate: 0.63
    - name: Shell of Rebuke
      pick_rate: 0.05
      win_rate: 0.67
  - name: Sage's Ring
    pick_rate: 0.09
    win_rate: 0.67
    alternates:
    - name: Medal of Defense
      pick_rate: 0.08
      win_rate: 0.59
    - name: Medal of Disruption
      pick_rate: 0.05
      win_rate: 0.62
  community_starters:
  - name: Selflessness
    pick_rate: 0.25
    win_rate: 0.56
  - name: Heroism
    pick_rate: 0.16
    win_rate: 0.65
  - name: Bluestone Pendant
    pick_rate: 0.13
    win_rate: 0.47
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-10-30'
  god_win_rate: 0.5424430641821946
  god_matches_won: 262
  god_matches_played: 483
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
  - Jotunn's Revenge
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Jotunn's Revenge
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Shifter''s Shield, Breastplate of Valor,
    Jotunn''s Revenge, Erosion, Eye of Providence, Draconic Scale, Berserker''s Shield,
    Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of
    the Storm, Gluttonous Grimoire, Helm of Radiance, Mantle Of Discord, Midgardian
    Mail, Runeforged Hammer, Oni Hunter''s Garb, Screeching Gargoyle, Prophetic Cloak,
    Leviathan''s Hide, Hide of the Nemean Lion, Void Shield, Ancile, Spear of Desolation,
    Spectral Armor, Helm of Darkness, Gladiator''s Shield, Hussar''s Wings, Void Stone,
    Xibalban Effigy, Rod of Asclepius, Hydra''s Lament, Daybreak Gavel, Kinetic Cuirass,
    Soul Gem, Doublet of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.66
      pick: 0.19
      fit: 0.38
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.27
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Shield of the Phoenix
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shifter's Shield
  - Jotunn's Revenge
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
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Rod of Asclepius,
    Shifter''s Shield, Jotunn''s Revenge, Soul Gem, Breastplate of Valor, Erosion,
    Berserker''s Shield, Eye of Providence, Draconic Scale, Ethereal Staff, Phoenix
    Feather, Yogi''s Necklace, Gluttonous Grimoire, Chandra''s Grace, Shield Splitter,
    Runeforged Hammer, Glorious Pridwen, Eye of the Storm, Midgardian Mail, Lifebinder,
    Oni Hunter''s Garb, Stone of Binding, Helm of Radiance, Leviathan''s Hide, Hide
    of the Nemean Lion, Void Shield, Ancile, Magi''s Cloak, Daybreak Gavel, Screeching
    Gargoyle, Gladiator''s Shield, Spear of Desolation, Spectral Armor, Sphere of
    Negation, Void Stone, Kinetic Cuirass.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.28
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.66
      pick: 0.19
      fit: 0.35
    Shield of the Phoenix:
      total: 0.59
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.58
      pick: 0.23
      fit: 0.55
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.65
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.95
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Freya's Tears
  - Jotunn's Revenge
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
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
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Screeching Gargoyle, Spear of Desolation, Void Shield, Spear
    of the Magus, Soul Gem, Breastplate of Valor, Void Stone, Obsidian Shard, Shifter''s
    Shield, Avenging Blade, Berserker''s Shield, Erosion, Eye of Providence, Shield
    Splitter, Heartseeker, Shield of the Phoenix, Draconic Scale, Doom Orb, Helm of
    Radiance, Runeforged Hammer, The World Stone, Titan''s Bane, The Crusher, Magi''s
    Cloak, Dreamer''s Idol, Eye of the Storm, Midgardian Mail, Mantle Of Discord,
    The Reaper, Oni Hunter''s Garb, Daybreak Gavel, Hydra''s Lament, Leviathan''s
    Hide, Hide of the Nemean Lion, Kinetic Cuirass.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.55
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.67
    Stone of Binding:
      total: 0.56
      efficiency: 0.5
      win: 0.6
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.58
      efficiency: 0.66
      win: 0.66
      pick: 0.19
      fit: 0.27
    Freya's Tears:
      total: 0.55
      efficiency: 0.61
      win: 0.58
      pick: 0.23
      fit: 0.44
    Jotunn's Revenge:
      total: 0.59
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.48
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.47
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Jotunn's Revenge
  - Nimble Ring
  - Amanita Charm
  flex_slots:
  - Nimble Ring
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Freya's Tears — magical protection
    swap_item: Freya's Tears
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Rod of Tahuti, Berserker''s Shield, Amanita Charm, Jotunn''s Revenge,
    Nimble Ring, Golden Blade, Gluttonous Grimoire, Breastplate of Valor, Tyrfing,
    Shifter''s Shield, Shield Splitter, Soul Gem, Pharaoh''s Curse, Runeforged Hammer,
    Riptalon, Lernaean Bow, Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance,
    Hydra''s Lament, Shield of the Phoenix, Eye of Providence, Toxic Blade, Eye of
    the Storm, Stone of Binding, Draconic Scale, Magi''s Cloak, Daybreak Gavel, Spear
    of Desolation, Screeching Gargoyle, Spear of the Magus, Midgardian Mail, The Reaper,
    Bragi''s Harp, Oni Hunter''s Garb, Tekko-Kagi, Rod of Asclepius, Mantle Of Discord,
    Kinetic Cuirass.'
  slot_scores:
    Golden Blade:
      total: 0.53
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.53
    Genji's Guard:
      total: 0.57
      efficiency: 0.66
      win: 0.66
      pick: 0.19
      fit: 0.21
    Berserker's Shield:
      total: 0.57
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.43
    Jotunn's Revenge:
      total: 0.55
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.54
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.29
    Amanita Charm:
      total: 0.55
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.36
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spear of Desolation
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Spear of Desolation
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Breastplate of Valor, Amanita Charm, Shield of the Phoenix, Spear of Desolation,
    Hydra''s Lament, Soul Gem, Lotus Sickle, Screeching Gargoyle, Shifter''s Shield,
    Chronos'' Pendant, Shield Splitter, Berserker''s Shield, Prophetic Cloak, Helm
    of Radiance, Erosion, Gluttonous Grimoire, Runeforged Hammer, Eye of Providence,
    Gladiator''s Shield, Draconic Scale, Stone of Binding, Eye of the Storm, Gem of
    Focus, Arondight, Magi''s Cloak, Spear of the Magus, Rod of Asclepius, Eye of
    Erebus, Midgardian Mail, Mantle Of Discord, Oni Hunter''s Garb, Glorious Pridwen,
    Daybreak Gavel, Obsidian Shard, Chandra''s Grace, Jade Scepter, Leviathan''s Hide,
    Kinetic Cuirass.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.48
    Genji's Guard:
      total: 0.61
      efficiency: 0.66
      win: 0.66
      pick: 0.19
      fit: 0.48
    Jotunn's Revenge:
      total: 0.58
      efficiency: 0.69
      win: 0.6
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.23
      fit: 0.64
    Spear of Desolation:
      total: 0.54
      efficiency: 0.58
      win: 0.6
      pick: 0.0
      fit: 0.46
    Amanita Charm:
      total: 0.57
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Genji's Guard
  - Freya's Tears
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
    Shield, Breastplate of Valor, Jotunn''s Revenge, Erosion, Eye of Providence, Draconic
    Scale, Berserker''s Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Eye of the Storm, Gluttonous Grimoire, Helm of Radiance, Mantle
    Of Discord, Midgardian Mail, Runeforged Hammer, Oni Hunter''s Garb, Screeching
    Gargoyle, Prophetic Cloak, Leviathan''s Hide, Hide of the Nemean Lion, Void Shield,
    Ancile, Spear of Desolation, Spectral Armor, Helm of Darkness, Gladiator''s Shield,
    Hussar''s Wings, Void Stone, Xibalban Effigy, Rod of Asclepius, Hydra''s Lament,
    Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.66
      pick: 0.19
      fit: 0.38
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.42
      pick: 0.11
      fit: 0.77
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: hybrid
  slot_order:
  - Gauntlet of Thebes
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Shell of Rebuke
  - Gauntlet of Thebes
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Genji's Guard — magical protection
    swap_item: Genji's Guard
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s core, corrected where the community is clearly right (efficiency
    + fit + win/pick). Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic
    Cuirass, Shifter''s Shield, Breastplate of Valor, Jotunn''s Revenge, Erosion,
    Eye of Providence, Draconic Scale, Berserker''s Shield, Shield Splitter, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm, Gluttonous
    Grimoire, Helm of Radiance, Mantle Of Discord, Midgardian Mail, Runeforged Hammer,
    Oni Hunter''s Garb, Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide, Hide
    of the Nemean Lion, Void Shield, Ancile, Spear of Desolation, Spectral Armor,
    Helm of Darkness, Gladiator''s Shield, Hussar''s Wings, Void Stone, Xibalban Effigy,
    Rod of Asclepius, Hydra''s Lament, Daybreak Gavel, Soul Gem, Doublet of Binding.'
  slot_scores:
    Gauntlet of Thebes:
      total: 0.42
      efficiency: 0.26
      win: 0.63
      pick: 0.27
      fit: 0.19
    Kinetic Cuirass:
      total: 0.51
      efficiency: 0.57
      win: 0.42
      pick: 0.11
      fit: 0.77
    Shell of Rebuke:
      total: 0.49
      efficiency: 0.28
      win: 0.68
      pick: 0.22
      fit: 0.48
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.58
      pick: 0.23
      fit: 0.62
    Shifter's Shield:
      total: 0.56
      efficiency: 0.55
      win: 0.6
      pick: 0.0
      fit: 0.67
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.6
      pick: 0.0
      fit: 0.67
  community_ordered:
  - Gauntlet of Thebes
  - Kinetic Cuirass
  - Shell of Rebuke
  - Freya's Tears
  swaps:
  - added: Shell of Rebuke
    removed: Breastplate of Valor
    reason: community 68% win over 63 matches (vs 54% on this god), taking the model's
      weakest slot from Breastplate of Valor
  - added: Gauntlet of Thebes
    removed: Genji's Guard
    reason: community 63% win over 130 matches (vs 54% on this god), taking the model's
      weakest slot from Genji's Guard
  starter: *id001
---
