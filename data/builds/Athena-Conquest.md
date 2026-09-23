---
type: smite-build
god: Athena
mode: Conquest
builds:
- source: community
  aspect: Aspect of War
  aspect_pick_rate: 0.15
  aspect_win_rate: 0.33
  slot_order:
  - name: Stampede
    pick_rate: 0.31
    win_rate: 0.61
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.27
      win_rate: 0.69
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.25
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 1.0
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.14
      win_rate: 0.63
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.5
  - name: Freya's Tears
    pick_rate: 0.18
    win_rate: 0.7
    alternates:
    - name: Genji's Guard
      pick_rate: 0.16
      win_rate: 0.33
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.6
  - name: Shell of Rebuke
    pick_rate: 0.22
    win_rate: 0.58
    alternates:
    - name: Freya's Tears
      pick_rate: 0.13
      win_rate: 0.71
    - name: Breastplate of Valor
      pick_rate: 0.13
      win_rate: 0.71
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.5
    alternates:
    - name: Genji's Guard
      pick_rate: 0.09
      win_rate: 0.6
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.8
  - name: Spectral Armor
    pick_rate: 0.06
    win_rate: 1.0
    alternates:
    - name: Freya's Tears
      pick_rate: 0.14
      win_rate: 0.6
    - name: Veve Charm
      pick_rate: 0.06
      win_rate: 1.0
  community_starters:
  - name: Selflessness
    pick_rate: 0.25
    win_rate: 0.6
  - name: Bumba's Cudgel
    pick_rate: 0.2
    win_rate: 0.33
  - name: Heroism
    pick_rate: 0.15
    win_rate: 0.78
  source_url: https://smitebrain.com/gods/athena/
  last_verified: '2026-09-23'
  god_win_rate: 0.559322033898305
  god_matches_won: 33
  god_matches_played: 59
  god_division: obsidian
  god_window_start: '2026-09-22'
  god_window_end: '2026-09-23'
  god_matches_analyzed: 962
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
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Kinetic Cuirass
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Jotunn''s Revenge, Erosion,
    Eye of Providence, Draconic Scale, Berserker''s Shield, Shield Splitter, Shield
    of the Phoenix, Stone of Binding, Magi''s Cloak, Eye of the Storm, Helm of Radiance,
    Gluttonous Grimoire, Mantle Of Discord, Midgardian Mail, Runeforged Hammer, Screeching
    Gargoyle, Prophetic Cloak, Leviathan''s Hide, Void Shield, Ancile, Oni Hunter''s
    Garb, Helm of Darkness, Xibalban Effigy, Void Stone, Spear of Desolation, Hussar''s
    Wings, Rod of Asclepius, Gladiator''s Shield, Daybreak Gavel, Soul Gem, Doublet
    of Binding, Hydra''s Lament, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.61
      efficiency: 0.65
      win: 0.71
      pick: 0.22
      fit: 0.37
    Genji's Guard:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.37
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.7
      pick: 0.28
      fit: 0.62
    Spectral Armor:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.44
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Spectral Armor
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Kinetic Cuirass
  - Genji's Guard
  - Shield of the Phoenix
  - Freya's Tears
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Kinetic Cuirass
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
    this god: Amanita Charm, Shield of the Phoenix, Rod of Tahuti, Kinetic Cuirass,
    Rod of Asclepius, Jotunn''s Revenge, Soul Gem, Berserker''s Shield, Erosion, Eye
    of Providence, Draconic Scale, Ethereal Staff, Phoenix Feather, Gluttonous Grimoire,
    Yogi''s Necklace, Shield Splitter, Chandra''s Grace, Runeforged Hammer, Glorious
    Pridwen, Eye of the Storm, Lifebinder, Midgardian Mail, Stone of Binding, Helm
    of Radiance, Leviathan''s Hide, Void Shield, Magi''s Cloak, Ancile, Oni Hunter''s
    Garb, Daybreak Gavel, Sphere of Negation, Screeching Gargoyle, Void Stone, Mantle
    Of Discord, Gladiator''s Shield, Shifter''s Shield.'
  slot_scores:
    Kinetic Cuirass:
      total: 0.62
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.76
    Genji's Guard:
      total: 0.74
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.34
    Shield of the Phoenix:
      total: 0.63
      efficiency: 0.53
      win: 0.69
      pick: 0.0
      fit: 0.9
    Freya's Tears:
      total: 0.63
      efficiency: 0.61
      win: 0.7
      pick: 0.28
      fit: 0.54
    Spectral Armor:
      total: 0.7
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.46
    Amanita Charm:
      total: 0.69
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.96
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Freya's Tears
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Jotunn''s Revenge, Amanita Charm, Stone of Binding,
    Gluttonous Grimoire, Kinetic Cuirass, Screeching Gargoyle, Spear of Desolation,
    Void Shield, Spear of the Magus, Soul Gem, Void Stone, Obsidian Shard, Avenging
    Blade, Berserker''s Shield, Heartseeker, Erosion, Shield Splitter, Eye of Providence,
    Draconic Scale, Shield of the Phoenix, Doom Orb, Helm of Radiance, Runeforged
    Hammer, The World Stone, Titan''s Bane, Magi''s Cloak, The Crusher, Dreamer''s
    Idol, Eye of the Storm, Mantle Of Discord, Midgardian Mail, The Reaper, Daybreak
    Gavel, Rod of Asclepius, Leviathan''s Hide, Hydra''s Lament, Shifter''s Shield.'
  slot_scores:
    Stone of Binding:
      total: 0.6
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.74
    Genji's Guard:
      total: 0.73
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.26
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.47
    Freya's Tears:
      total: 0.61
      efficiency: 0.61
      win: 0.7
      pick: 0.28
      fit: 0.43
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.31
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.48
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Genji's Guard
  - Berserker's Shield
  - Nimble Ring
  - Spectral Armor
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
    Nimble Ring, Kinetic Cuirass, Golden Blade, Gluttonous Grimoire, Tyrfing, Shield
    Splitter, Soul Gem, Runeforged Hammer, Pharaoh''s Curse, Riptalon, Lernaean Bow,
    Shogun''s Ofuda, Silverbranch Bow, Erosion, Helm of Radiance, Eye of Providence,
    Stone of Binding, Eye of the Storm, Shield of the Phoenix, Hydra''s Lament, Toxic
    Blade, Draconic Scale, Magi''s Cloak, Screeching Gargoyle, Daybreak Gavel, The
    Reaper, Spear of Desolation, Spear of the Magus, Bragi''s Harp, Midgardian Mail,
    Mantle Of Discord, Tekko-Kagi, Rod of Asclepius, Avenging Blade, Shifter''s Shield.'
  slot_scores:
    Golden Blade:
      total: 0.57
      efficiency: 0.52
      win: 0.69
      pick: 0.0
      fit: 0.54
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.2
    Berserker's Shield:
      total: 0.62
      efficiency: 0.68
      win: 0.69
      pick: 0.0
      fit: 0.43
    Nimble Ring:
      total: 0.58
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.3
    Spectral Armor:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.24
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.37
  community_ordered:
  - Genji's Guard
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Breastplate of Valor
  - Amanita Charm
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
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Shield of the Phoenix, Spear of Desolation, Hydra''s
    Lament, Screeching Gargoyle, Soul Gem, Chronos'' Pendant, Shield Splitter, Berserker''s
    Shield, Prophetic Cloak, Erosion, Helm of Radiance, Runeforged Hammer, Gluttonous
    Grimoire, Eye of Providence, Gladiator''s Shield, Draconic Scale, Stone of Binding,
    Eye of the Storm, Arondight, Gem of Focus, Magi''s Cloak, Rod of Asclepius, Eye
    of Erebus, Spear of the Magus, Mantle Of Discord, Glorious Pridwen, Midgardian
    Mail, Daybreak Gavel, Chandra''s Grace, Obsidian Shard, Leviathan''s Hide, Jade
    Scepter, Void Shield, Shifter''s Shield.'
  slot_scores:
    Breastplate of Valor:
      total: 0.63
      efficiency: 0.65
      win: 0.71
      pick: 0.22
      fit: 0.48
    Genji's Guard:
      total: 0.76
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.48
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.46
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.7
      pick: 0.28
      fit: 0.64
    Spectral Armor:
      total: 0.68
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.29
    Amanita Charm:
      total: 0.61
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.45
  community_ordered:
  - Breastplate of Valor
  - Genji's Guard
  - Freya's Tears
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Genji's Guard
  - Jotunn's Revenge
  - Freya's Tears
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Freya's Tears
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Magi's Cloak — CC-immunity / cleanse
    swap_item: Magi's Cloak
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge, Berserker''s
    Shield, Amanita Charm, Kinetic Cuirass, Shield Splitter, Runeforged Hammer, Golden
    Blade, Eye of the Storm, Gluttonous Grimoire, Hydra''s Lament, Heartseeker, Tyrfing,
    Lernaean Bow, Erosion, Spear of Desolation, Tekko-Kagi, Spear of the Magus, Eye
    of Providence, Avenging Blade, Shield of the Phoenix, Stone of Binding, Draconic
    Scale, Helm of Radiance, Soul Gem, Titan''s Bane, Silverbranch Bow, The Crusher,
    Obsidian Shard, Pharaoh''s Curse, Magi''s Cloak, Toxic Blade, The Reaper, Nimble
    Ring, Shogun''s Ofuda, Screeching Gargoyle, Mantle Of Discord, Midgardian Mail,
    Shifter''s Shield.'
  slot_scores:
    Berserker's Shield:
      total: 0.6
      efficiency: 0.68
      win: 0.69
      pick: 0.0
      fit: 0.36
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.63
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.6
      efficiency: 0.61
      win: 0.7
      pick: 0.28
      fit: 0.38
    Spectral Armor:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.27
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Book of Thoth
  - Genji's Guard
  - Jotunn's Revenge
  - Transcendence
  - Spectral Armor
  - Amanita Charm
  flex_slots:
  - Transcendence
  - Book of Thoth
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
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Rod of Tahuti, Jotunn''s Revenge,
    Amanita Charm, Kinetic Cuirass, Gluttonous Grimoire, Shield Splitter, Spear of
    Desolation, Spear of the Magus, Runeforged Hammer, Helm of Radiance, Soul Gem,
    Obsidian Shard, Berserker''s Shield, Eye of the Storm, Hydra''s Lament, Rod of
    Asclepius, Heartseeker, Erosion, Eye of Providence, Shield of the Phoenix, Stone
    of Binding, Draconic Scale, Doom Orb, Jade Scepter, Death Metal, Wish-Granting
    Pearl, Avenging Blade, Magi''s Cloak, Chronos'' Pendant, The World Stone, Helm
    of Darkness, Titan''s Bane, The Crusher, Ancient Signet, Screeching Gargoyle,
    Mantle Of Discord, Dreamer''s Idol, Midgardian Mail, Shifter''s Shield.'
  slot_scores:
    Book of Thoth:
      total: 0.52
      efficiency: 0.51
      win: 0.69
      pick: 0.0
      fit: 0.18
    Genji's Guard:
      total: 0.72
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.23
    Jotunn's Revenge:
      total: 0.62
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.41
    Transcendence:
      total: 0.52
      efficiency: 0.53
      win: 0.69
      pick: 0.0
      fit: 0.18
    Spectral Armor:
      total: 0.67
      efficiency: 0.5
      win: 1.0
      pick: 0.18
      fit: 0.27
    Amanita Charm:
      total: 0.6
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.42
  community_ordered:
  - Genji's Guard
  - Spectral Armor
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Jotunn's Revenge
  - Genji's Guard
  - Kinetic Cuirass
  - Freya's Tears
  - Shifter's Shield
  - Amanita Charm
  flex_slots:
  - Jotunn's Revenge
  - Genji's Guard
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
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Amanita Charm, Rod of Tahuti, Kinetic Cuirass, Shifter''s
    Shield, Jotunn''s Revenge, Erosion, Eye of Providence, Draconic Scale, Berserker''s
    Shield, Shield Splitter, Shield of the Phoenix, Stone of Binding, Magi''s Cloak,
    Eye of the Storm, Helm of Radiance, Gluttonous Grimoire, Mantle Of Discord, Midgardian
    Mail, Runeforged Hammer, Screeching Gargoyle, Prophetic Cloak, Leviathan''s Hide,
    Void Shield, Ancile, Oni Hunter''s Garb, Helm of Darkness, Xibalban Effigy, Void
    Stone, Spear of Desolation, Hussar''s Wings, Rod of Asclepius, Gladiator''s Shield,
    Daybreak Gavel, Soul Gem, Doublet of Binding, Hydra''s Lament.'
  slot_scores:
    Jotunn's Revenge:
      total: 0.6
      efficiency: 0.72
      win: 0.69
      pick: 0.0
      fit: 0.25
    Genji's Guard:
      total: 0.75
      efficiency: 0.66
      win: 1.0
      pick: 0.2
      fit: 0.37
    Kinetic Cuirass:
      total: 0.63
      efficiency: 0.56
      win: 0.69
      pick: 0.0
      fit: 0.78
    Freya's Tears:
      total: 0.64
      efficiency: 0.61
      win: 0.7
      pick: 0.28
      fit: 0.62
    Shifter's Shield:
      total: 0.41
      efficiency: 0.55
      win: 0.25
      pick: 0.14
      fit: 0.68
    Amanita Charm:
      total: 0.64
      efficiency: 0.65
      win: 0.69
      pick: 0.0
      fit: 0.68
  community_ordered:
  - Genji's Guard
  - Freya's Tears
  - Shifter's Shield
  starter: *id001
---
