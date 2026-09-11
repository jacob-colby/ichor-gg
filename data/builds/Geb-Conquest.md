---
type: smite-build
god: Geb
mode: Conquest
builds:
- source: community
  aspect: Aspect of Calamity
  aspect_pick_rate: 0.03
  aspect_win_rate: 0.0
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.21
    win_rate: 0.71
    alternates:
    - name: Stampede
      pick_rate: 0.19
      win_rate: 0.67
    - name: Chandra's Grace
      pick_rate: 0.15
      win_rate: 0.58
  - name: Genji's Guard
    pick_rate: 0.2
    win_rate: 0.69
    alternates:
    - name: Chandra's Grace
      pick_rate: 0.13
      win_rate: 0.7
    - name: Stampede
      pick_rate: 0.1
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.22
    win_rate: 0.53
    alternates:
    - name: Genji's Guard
      pick_rate: 0.14
      win_rate: 0.64
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.71
  - name: Draconic Scale
    pick_rate: 0.11
    win_rate: 0.63
    alternates:
    - name: Freya's Tears
      pick_rate: 0.18
      win_rate: 0.54
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 1.0
  - name: Shell of Rebuke
    pick_rate: 0.1
    win_rate: 0.5
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.88
    - name: Veve Charm
      pick_rate: 0.1
      win_rate: 0.5
  - name: Medallion
    pick_rate: 0.21
    win_rate: 0.71
    alternates:
    - name: Hide of the Nemean Lion
      pick_rate: 0.12
      win_rate: 0.5
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.4
    win_rate: 0.53
  - name: Heroism
    pick_rate: 0.28
    win_rate: 0.68
  - name: Conduit Gem
    pick_rate: 0.08
    win_rate: 0.33
  source_url: https://smitebrain.com/gods/geb/
  last_verified: '2026-09-11'
  god_win_rate: 0.625
  god_matches_won: 50
  god_matches_played: 80
  god_division: obsidian
  god_window_start: '2026-09-08'
  god_window_end: '2026-09-11'
  god_matches_analyzed: 3080
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion, Eye of Providence,
    Breastplate of Valor, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Mantle Of Discord, Prophetic Cloak, Midgardian Mail, Hussar''s Wings, Leviathan''s
    Hide, Screeching Gargoyle, Void Shield, Ancile, Oni Hunter''s Garb, Xibalban Effigy,
    Gladiator''s Shield, Void Stone, Spectral Armor, Doublet of Binding, Stygian Anchor.'
  slot_scores:
    Eye of Providence:
      total: 0.6
      efficiency: 0.61
      win: 0.65
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.69
      pick: 0.27
      fit: 0.45
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.95
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Genji's Guard
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
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
    swap: Eye of Providence — magical protection
    swap_item: Eye of Providence
  - vs_tag: physical_heavy
    swap: Draconic Scale — physical protection
    swap_item: Draconic Scale
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Shifter''s Shield,
    Erosion, Eye of Providence, Breastplate of Valor, Phoenix Feather, Glorious Pridwen,
    Yogi''s Necklace, Midgardian Mail, Stone of Binding, Leviathan''s Hide, Void Shield,
    Ancile, Oni Hunter''s Garb, Gladiator''s Shield, Magi''s Cloak, Hussar''s Wings,
    Void Stone, Spectral Armor, Mantle Of Discord, Screeching Gargoyle.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.94
    Genji's Guard:
      total: 0.62
      efficiency: 0.66
      win: 0.69
      pick: 0.27
      fit: 0.42
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.53
      win: 0.65
      pick: 0.0
      fit: 1.0
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.84
    Amanita Charm:
      total: 0.67
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 1.0
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.84
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Screeching Gargoyle
  - Stone of Binding
  - Genji's Guard
  - Kinetic Cuirass
  - Void Shield
  - Amanita Charm
  flex_slots:
  - Screeching Gargoyle
  - Void Shield
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Amanita Charm, Stone of Binding, Kinetic Cuirass, Screeching Gargoyle,
    Void Shield, Shifter''s Shield, Breastplate of Valor, Void Stone, Erosion, Eye
    of Providence, Shield of the Phoenix, Magi''s Cloak, Mantle Of Discord, Midgardian
    Mail, Gluttonous Grimoire, Leviathan''s Hide, Ancile, Oni Hunter''s Garb, Prophetic
    Cloak, Spectral Armor, Xibalban Effigy, Doublet of Binding, Gladiator''s Shield,
    Hussar''s Wings.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.57
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.68
    Stone of Binding:
      total: 0.59
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.78
    Genji's Guard:
      total: 0.6
      efficiency: 0.66
      win: 0.69
      pick: 0.27
      fit: 0.28
    Kinetic Cuirass:
      total: 0.58
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.63
    Void Shield:
      total: 0.57
      efficiency: 0.47
      win: 0.65
      pick: 0.0
      fit: 0.74
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.53
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
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
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Kinetic Cuirass, Breastplate of Valor, Shifter''s Shield,
    Erosion, Eye of Providence, Nimble Ring, Stone of Binding, Shield of the Phoenix,
    Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, Mantle Of Discord, Midgardian
    Mail, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s Garb, Void Stone,
    Spectral Armor, Xibalban Effigy, Prophetic Cloak, Doublet of Binding, Gladiator''s
    Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.49
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.69
      pick: 0.27
      fit: 0.21
    Bracer of The Abyss:
      total: 0.45
      efficiency: 0.35
      win: 0.65
      pick: 0.0
      fit: 0.21
    Nimble Ring:
      total: 0.53
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.28
    Bragi's Harp:
      total: 0.49
      efficiency: 0.37
      win: 0.65
      pick: 0.0
      fit: 0.42
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.39
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Screeching Gargoyle
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Shield of the Phoenix
  flex_slots:
  - Freya's Tears
  - Screeching Gargoyle
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shifter's Shield — physical protection
    swap_item: Shifter's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Amanita Charm,
    Rod of Tahuti, Kinetic Cuirass, Shield of the Phoenix, Screeching Gargoyle, Shifter''s
    Shield, Chronos'' Pendant, Prophetic Cloak, Erosion, Helm of Radiance, Gladiator''s
    Shield, Eye of Providence, Soul Gem, Stone of Binding, Gem of Focus, Spear of
    Desolation, Magi''s Cloak, Eye of Erebus, Rod of Asclepius, Glorious Pridwen,
    Mantle Of Discord, Midgardian Mail, Daybreak Gavel.'
  slot_scores:
    Screeching Gargoyle:
      total: 0.56
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.6
    Genji's Guard:
      total: 0.63
      efficiency: 0.66
      win: 0.69
      pick: 0.27
      fit: 0.5
    Breastplate of Valor:
      total: 0.6
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.5
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.57
      efficiency: 0.61
      win: 0.53
      pick: 0.34
      fit: 0.67
    Shield of the Phoenix:
      total: 0.57
      efficiency: 0.53
      win: 0.65
      pick: 0.0
      fit: 0.63
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield Splitter
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
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Jotunn''s Revenge, Amanita Charm, Berserker''s
    Shield, Kinetic Cuirass, Shield Splitter, Golden Blade, Runeforged Hammer, Breastplate
    of Valor, Shifter''s Shield, Eye of the Storm, Tyrfing, Heartseeker, Hydra''s
    Lament, Erosion, Lernaean Bow, Tekko-Kagi, Eye of Providence, Avenging Blade,
    Silverbranch Bow, Stone of Binding, Shield of the Phoenix, Titan''s Bane, The
    Crusher, Toxic Blade, Pharaoh''s Curse, Magi''s Cloak, The Reaper, Shogun''s Ofuda,
    Mantle Of Discord, Screeching Gargoyle, Midgardian Mail, Daybreak Gavel, Arondight,
    Leviathan''s Hide, Void Shield, Dominance, Ancile.'
  slot_scores:
    Berserker's Shield:
      total: 0.59
      efficiency: 0.68
      win: 0.65
      pick: 0.0
      fit: 0.37
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.69
      pick: 0.27
      fit: 0.23
    Jotunn's Revenge:
      total: 0.61
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.47
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.54
    Shield Splitter:
      total: 0.57
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.55
    Amanita Charm:
      total: 0.59
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.44
  community_ordered:
  - Genji's Guard
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
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Breastplate
    of Valor, Spear of Desolation, Spear of the Magus, Runeforged Hammer, Helm of
    Radiance, Soul Gem, Shifter''s Shield, Obsidian Shard, Berserker''s Shield, Eye
    of the Storm, Rod of Asclepius, Hydra''s Lament, Heartseeker, Erosion, Eye of
    Providence, Stone of Binding, Shield of the Phoenix, Doom Orb, Jade Scepter, Death
    Metal, Wish-Granting Pearl, Avenging Blade, Magi''s Cloak, The World Stone, Helm
    of Darkness, Chronos'' Pendant, Titan''s Bane, The Crusher, Ancient Signet, Screeching
    Gargoyle, Mantle Of Discord, Dreamer''s Idol, Midgardian Mail.'
  slot_scores:
    Book of Thoth:
      total: 0.5
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.59
      efficiency: 0.66
      win: 0.69
      pick: 0.27
      fit: 0.22
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.65
      pick: 0.0
      fit: 0.4
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.52
    Transcendence:
      total: 0.5
      efficiency: 0.53
      win: 0.65
      pick: 0.0
      fit: 0.18
    Amanita Charm:
      total: 0.58
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Draconic Scale — magical protection
    swap_item: Draconic Scale
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Kinetic Cuirass, Shifter''s Shield, Erosion,
    Eye of Providence, Breastplate of Valor, Shield of the Phoenix, Stone of Binding,
    Magi''s Cloak, Mantle Of Discord, Prophetic Cloak, Midgardian Mail, Hussar''s
    Wings, Leviathan''s Hide, Screeching Gargoyle, Void Shield, Ancile, Oni Hunter''s
    Garb, Xibalban Effigy, Gladiator''s Shield, Void Stone, Spectral Armor, Doublet
    of Binding, Stygian Anchor.'
  slot_scores:
    Eye of Providence:
      total: 0.6
      efficiency: 0.61
      win: 0.65
      pick: 0.0
      fit: 0.6
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.65
      pick: 0.0
      fit: 0.95
    Freya's Tears:
      total: 0.58
      efficiency: 0.61
      win: 0.53
      pick: 0.34
      fit: 0.76
    Shifter's Shield:
      total: 0.61
      efficiency: 0.55
      win: 0.65
      pick: 0.0
      fit: 0.85
    Amanita Charm:
      total: 0.65
      efficiency: 0.65
      win: 0.65
      pick: 0.0
      fit: 0.85
    Erosion:
      total: 0.6
      efficiency: 0.51
      win: 0.65
      pick: 0.0
      fit: 0.85
  community_ordered:
  - Freya's Tears
  starter: *id001
---
