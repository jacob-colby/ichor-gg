---
type: smite-build
god: Ares
mode: Conquest
builds:
- source: community
  aspect: Aspect of Reverberation
  aspect_pick_rate: 0.09
  aspect_win_rate: 0.63
  slot_order:
  - name: Gauntlet of Thebes
    pick_rate: 0.16
    win_rate: 0.6
    alternates:
    - name: Shifter's Shield
      pick_rate: 0.14
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.14
      win_rate: 0.57
  - name: Genji's Guard
    pick_rate: 0.17
    win_rate: 0.46
    alternates:
    - name: Stampede
      pick_rate: 0.16
      win_rate: 0.61
    - name: Prophetic Cloak
      pick_rate: 0.07
      win_rate: 0.62
  - name: Stampede
    pick_rate: 0.12
    win_rate: 0.61
    alternates:
    - name: Genji's Guard
      pick_rate: 0.13
      win_rate: 0.56
    - name: Shell of Rebuke
      pick_rate: 0.09
      win_rate: 0.52
  - name: Shell of Rebuke
    pick_rate: 0.11
    win_rate: 0.6
    alternates:
    - name: Genji's Guard
      pick_rate: 0.08
      win_rate: 0.77
    - name: Freya's Tears
      pick_rate: 0.08
      win_rate: 0.7
  - name: Hide of the Nemean Lion
    pick_rate: 0.08
    win_rate: 0.59
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.08
      win_rate: 0.61
    - name: Spirit Robe
      pick_rate: 0.07
      win_rate: 0.71
  - name: Engraved Guard
    pick_rate: 0.08
    win_rate: 0.45
    alternates:
    - name: Veve Charm
      pick_rate: 0.07
      win_rate: 0.8
    - name: Medallion
      pick_rate: 0.06
      win_rate: 0.88
  community_starters:
  - name: Selflessness
    pick_rate: 0.25
    win_rate: 0.61
  - name: Warrior's Axe
    pick_rate: 0.2
    win_rate: 0.53
  - name: Heroism
    pick_rate: 0.15
    win_rate: 0.63
  source_url: https://smitebrain.com/gods/ares/
  last_verified: '2026-08-19'
  god_win_rate: 0.5798611111111112
  god_matches_won: 167
  god_matches_played: 288
  god_division: obsidian
  god_window_start: '2026-08-11'
  god_window_end: '2026-08-19'
  god_matches_analyzed: 10108
  starter:
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: core
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Erosion
  - Breastplate of Valor
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Oni Hunter's Garb — magical protection
    swap_item: Oni Hunter's Garb
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Kinetic Cuirass, Amanita Charm, Berserker''s Shield,
    Rod of Tahuti, Shield of the Phoenix, Gluttonous Grimoire, Erosion, Breastplate
    of Valor, Oni Hunter''s Garb, Eye of Providence, Draconic Scale, Spectral Armor,
    Jotunn''s Revenge, Shield Splitter, Shifter''s Shield, The Crusher, Pharaoh''s
    Curse, Leviathan''s Hide, Prophetic Cloak, Soul Gem, Mantle Of Discord, Midgardian
    Mail, Stone of Binding, Eye of the Storm, Nimble Ring, Runeforged Hammer, Magi''s
    Cloak, Gladiator''s Shield, Screeching Gargoyle, Ancile, Hydra''s Lament, Shogun''s
    Ofuda, Void Shield, Helm of Radiance, Doublet of Binding, Chandra''s Grace, Hussar''s
    Wings.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.43
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.38
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.67
    Erosion:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.67
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Berserker's Shield
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Berserker's Shield
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Stampede — CC-immunity / cleanse
    swap_item: Stampede
  - vs_tag: magic_heavy
    swap: Spirit Robe — magical protection
    swap_item: Spirit Robe
  - vs_tag: physical_heavy
    swap: Erosion — physical protection
    swap_item: Erosion
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Freya''s Tears, Shield of the Phoenix, Kinetic Cuirass,
    Soul Gem, Berserker''s Shield, Gluttonous Grimoire, Chandra''s Grace, Rod of Tahuti,
    Rod of Asclepius, Oni Hunter''s Garb, Erosion, Eye of Providence, Breastplate
    of Valor, Phoenix Feather, Draconic Scale, Spectral Armor, Jotunn''s Revenge,
    Pharaoh''s Curse, The Crusher, Leviathan''s Hide, Shifter''s Shield, Midgardian
    Mail, Runeforged Hammer, Glorious Pridwen, Eye of the Storm, Lifebinder, Gladiator''s
    Shield, Shield Splitter, Nimble Ring, Ancile, The Reaper, Blood-Bound Book, Shogun''s
    Ofuda, Void Shield, Hydra''s Lament, Doublet of Binding, Mantle Of Discord, Bancroft''s
    Talon.'
  slot_scores:
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.45
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.75
    Shield of the Phoenix:
      total: 0.61
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.9
    Oni Hunter's Garb:
      total: 0.55
      efficiency: 0.61
      win: 0.6
      pick: 0.0
      fit: 0.45
    Freya's Tears:
      total: 0.61
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.55
    Amanita Charm:
      total: 0.64
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.95
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Stone of Binding
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Freya's Tears
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Kinetic Cuirass
  - Stone of Binding
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Rod of Tahuti, Freya''s Tears, Gluttonous Grimoire, The Crusher,
    Jotunn''s Revenge, Kinetic Cuirass, Amanita Charm, Soul Gem, Stone of Binding,
    Berserker''s Shield, Screeching Gargoyle, Void Shield, Breastplate of Valor, The
    Cosmic Horror, Oni Hunter''s Garb, Shield of the Phoenix, Void Stone, Spear of
    the Magus, Spear of Desolation, Avenging Blade, Erosion, Eye of Providence, Spectral
    Armor, Nimble Ring, Draconic Scale, The Reaper, Obsidian Shard, Pharaoh''s Curse,
    Riptalon, Shield Splitter, Leviathan''s Hide, Runeforged Hammer, Midgardian Mail,
    Silverbranch Bow, Hydra''s Lament, Mantle Of Discord, Shifter''s Shield, Eye of
    the Storm, Helm of Radiance, Ancile.'
  slot_scores:
    Stone of Binding:
      total: 0.55
      efficiency: 0.47
      win: 0.6
      pick: 0.0
      fit: 0.74
    Jotunn's Revenge:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.48
    Kinetic Cuirass:
      total: 0.57
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.57
    Freya's Tears:
      total: 0.59
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.44
    Gluttonous Grimoire:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.62
    The Crusher:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.48
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Golden Blade
  - Berserker's Shield
  - Kinetic Cuirass
  - Nimble Ring
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Amanita Charm
  - Golden Blade
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Pharaoh's Curse — magical protection
    swap_item: Pharaoh's Curse
  - vs_tag: physical_heavy
    swap: Breastplate of Valor — physical protection
    swap_item: Breastplate of Valor
  - vs_tag: sustain
    swap: Toxic Blade — anti-heal
    swap_item: Toxic Blade
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Freya''s Tears, Berserker''s Shield, Nimble Ring, Rod of Tahuti, Kinetic
    Cuirass, Amanita Charm, Gluttonous Grimoire, Golden Blade, The Crusher, Pharaoh''s
    Curse, Jotunn''s Revenge, Breastplate of Valor, Riptalon, Oni Hunter''s Garb,
    Soul Gem, Shield of the Phoenix, Shogun''s Ofuda, Tyrfing, Runeforged Hammer,
    Spectral Armor, Hydra''s Lament, Erosion, Lernaean Bow, Silverbranch Bow, Shield
    Splitter, Eye of Providence, Draconic Scale, Eye of the Storm, Leviathan''s Hide,
    Midgardian Mail, Mantle Of Discord, Toxic Blade, Stone of Binding, Helm of Radiance,
    Screeching Gargoyle, Death Metal, Yogi''s Necklace, Damaru, Ancile, Shifter''s
    Shield.'
  slot_scores:
    Golden Blade:
      total: 0.54
      efficiency: 0.53
      win: 0.6
      pick: 0.0
      fit: 0.53
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.55
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.46
    Nimble Ring:
      total: 0.56
      efficiency: 0.68
      win: 0.6
      pick: 0.0
      fit: 0.29
    Freya's Tears:
      total: 0.58
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.34
    Amanita Charm:
      total: 0.55
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.36
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Hydra's Lament
  - Freya's Tears
  flex_slots:
  - Shield of the Phoenix
  - Hydra's Lament
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Berserker's Shield — physical protection
    swap_item: Berserker's Shield
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Freya''s Tears, Breastplate of Valor,
    Jotunn''s Revenge, Kinetic Cuirass, Shield of the Phoenix, Rod of Tahuti, Amanita
    Charm, Soul Gem, Gluttonous Grimoire, Hydra''s Lament, Berserker''s Shield, The
    Crusher, Screeching Gargoyle, Oni Hunter''s Garb, Prophetic Cloak, Chronos'' Pendant,
    Nimble Ring, Chandra''s Grace, Spear of Desolation, Gladiator''s Shield, Erosion,
    Spectral Armor, Eye of Providence, Shield Splitter, Draconic Scale, Runeforged
    Hammer, Pharaoh''s Curse, Eye of the Storm, Leviathan''s Hide, Gem of Focus, Helm
    of Radiance, Midgardian Mail, Mantle Of Discord, Totem of Death, Stone of Binding,
    Arondight, Shifter''s Shield, Death Metal, Rod of Asclepius, The Cosmic Horror.'
  slot_scores:
    Breastplate of Valor:
      total: 0.57
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.48
    Jotunn's Revenge:
      total: 0.56
      efficiency: 0.64
      win: 0.6
      pick: 0.0
      fit: 0.46
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.56
      efficiency: 0.57
      win: 0.6
      pick: 0.0
      fit: 0.61
    Hydra's Lament:
      total: 0.54
      efficiency: 0.56
      win: 0.6
      pick: 0.0
      fit: 0.52
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Genji's Guard
  - Berserker's Shield
  - Kinetic Cuirass
  - Freya's Tears
  - Amanita Charm
  - Erosion
  flex_slots:
  - Berserker's Shield
  - Erosion
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Stygian Anchor — anti-heal
    swap_item: Stygian Anchor
  rationale: 'The model''s own answer — no meta signal (efficiency + fit + win/pick).
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Freya''s Tears, Berserker''s
    Shield, Rod of Tahuti, Shield of the Phoenix, Gluttonous Grimoire, Erosion, Shifter''s
    Shield, Breastplate of Valor, Oni Hunter''s Garb, Eye of Providence, Draconic
    Scale, Spectral Armor, Jotunn''s Revenge, Shield Splitter, The Crusher, Pharaoh''s
    Curse, Leviathan''s Hide, Soul Gem, Mantle Of Discord, Midgardian Mail, Stone
    of Binding, Eye of the Storm, Nimble Ring, Runeforged Hammer, Magi''s Cloak, Gladiator''s
    Shield, Screeching Gargoyle, Ancile, Prophetic Cloak, Hydra''s Lament, Shogun''s
    Ofuda, Void Shield, Helm of Radiance, Doublet of Binding, Chandra''s Grace, Hussar''s
    Wings.'
  slot_scores:
    Genji's Guard:
      total: 0.52
      efficiency: 0.69
      win: 0.46
      pick: 0.23
      fit: 0.38
    Berserker's Shield:
      total: 0.57
      efficiency: 0.66
      win: 0.6
      pick: 0.0
      fit: 0.43
    Kinetic Cuirass:
      total: 0.59
      efficiency: 0.59
      win: 0.6
      pick: 0.0
      fit: 0.77
    Freya's Tears:
      total: 0.62
      efficiency: 0.59
      win: 0.7
      pick: 0.13
      fit: 0.62
    Amanita Charm:
      total: 0.59
      efficiency: 0.63
      win: 0.6
      pick: 0.0
      fit: 0.67
    Erosion:
      total: 0.55
      efficiency: 0.52
      win: 0.6
      pick: 0.0
      fit: 0.67
  starter: *id001
---
