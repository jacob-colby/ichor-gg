---
type: smite-build
god: Yemoja
mode: Conquest
builds:
- source: community
  aspect: Aspect of Downpour
  aspect_pick_rate: 0.08
  aspect_win_rate: 0.5
  slot_order:
  - name: Spear of Desolation
    pick_rate: 0.12
    win_rate: 0.39
    alternates:
    - name: Gauntlet of Thebes
      pick_rate: 0.11
      win_rate: 0.44
    - name: Chandra's Grace
      pick_rate: 0.1
      win_rate: 0.6
  - name: Genji's Guard
    pick_rate: 0.15
    win_rate: 0.43
    alternates:
    - name: Spear of Desolation
      pick_rate: 0.23
      win_rate: 0.59
    - name: Breastplate of Valor
      pick_rate: 0.07
      win_rate: 0.7
  - name: Breastplate of Valor
    pick_rate: 0.14
    win_rate: 0.62
    alternates:
    - name: Genji's Guard
      pick_rate: 0.18
      win_rate: 0.54
    - name: Stampede
      pick_rate: 0.06
      win_rate: 0.78
  - name: Shell of Rebuke
    pick_rate: 0.09
    win_rate: 0.5
    alternates:
    - name: Breastplate of Valor
      pick_rate: 0.1
      win_rate: 0.5
    - name: Genji's Guard
      pick_rate: 0.07
      win_rate: 0.8
  - name: Mote of Chaos
    pick_rate: 0.07
    win_rate: 0.5
    alternates:
    - name: Shell of Rebuke
      pick_rate: 0.13
      win_rate: 0.53
    - name: Dwarven Plate
      pick_rate: 0.05
      win_rate: 0.5
  - name: Engraved Guard
    pick_rate: 0.1
    win_rate: 0.75
    alternates:
    - name: Captain's Ring
      pick_rate: 0.05
      win_rate: 0.75
    - name: Shield
      pick_rate: 0.05
      win_rate: 0.75
  source_url: https://smitebrain.com/gods/yemoja/
  last_verified: '2026-08-01'
  god_win_rate: 0.5167785234899329
  god_matches_won: 77
  god_matches_played: 149
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
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Freya's Tears
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
  rationale: 'Top weighted-score core (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Kinetic Cuirass, Amanita Charm, Eye of Providence,
    Gluttonous Grimoire, Oni Hunter''s Garb, Shield of the Phoenix, Freya''s Tears,
    Shifter''s Shield, Ethereal Staff, Spectral Armor, Genji''s Guard, Erosion, Mantle
    Of Discord, Soul Gem, Draconic Scale, Wish-Granting Pearl, Leviathan''s Hide,
    Jade Scepter, Yogi''s Necklace, Rod of Asclepius, Hussar''s Wings, Midgardian
    Mail, Helm of Radiance, Chandra''s Grace, Hide of the Nemean Lion, Gladiator''s
    Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: &id001
    base: Warrior's Axe
    upgrade: Sundering Axe
- source: suggested
  archetype: bruiser
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Oni Hunter's Garb
  - Amanita Charm
  flex_slots:
  - Eye of Providence
  - Oni Hunter's Garb
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Shifter's Shield — magical protection
    swap_item: Shifter's Shield
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Lifesteal bruiser skew (efficiency + fit + win/pick). Underrated for
    this god: Amanita Charm, Breastplate of Valor, Shield of the Phoenix, Soul Gem,
    Kinetic Cuirass, Gluttonous Grimoire, Rod of Asclepius, Eye of Providence, Chandra''s
    Grace, Oni Hunter''s Garb, Ethereal Staff, Spectral Armor, Shifter''s Shield,
    Lifebinder, Freya''s Tears, Bancroft''s Talon, Genji''s Guard, Erosion, Phoenix
    Feather, Blood-Bound Book, Draconic Scale, Wish-Granting Pearl, Jade Scepter,
    Yogi''s Necklace, Mantle Of Discord, Leviathan''s Hide, Spirit Robe.'
  slot_scores:
    Eye of Providence:
      total: 0.54
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.62
    Breastplate of Valor:
      total: 0.58
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.36
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.72
    Shield of the Phoenix:
      total: 0.58
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.9
    Oni Hunter's Garb:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.43
    Amanita Charm:
      total: 0.6
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.92
  starter: *id001
- source: suggested
  archetype: anti-tank
  slot_order:
  - Eye of Providence
  - Breastplate of Valor
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Ethereal Staff
  - Gluttonous Grimoire
  flex_slots:
  - Oni Hunter's Garb
  - Ethereal Staff
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Shield of the Phoenix — physical protection
    swap_item: Shield of the Phoenix
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Full-penetration anti-tank skew (efficiency + fit + win/pick). Underrated
    for this god: Gluttonous Grimoire, Breastplate of Valor, Soul Gem, Kinetic Cuirass,
    Amanita Charm, Eye of Providence, Oni Hunter''s Garb, Ethereal Staff, Spear of
    the Magus, Shield of the Phoenix, Spectral Armor, Stone of Binding, Void Shield,
    Screeching Gargoyle, Genji''s Guard, Freya''s Tears, Shifter''s Shield, Mantle
    Of Discord, The Cosmic Horror, Void Stone, Erosion, Yogi''s Necklace, Draconic
    Scale, Wish-Granting Pearl, Jade Scepter, Obsidian Shard, Spear of Desolation.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.28
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Oni Hunter's Garb:
      total: 0.52
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.29
    Ethereal Staff:
      total: 0.51
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.23
    Gluttonous Grimoire:
      total: 0.57
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.66
  starter: *id001
- source: suggested
  archetype: attack-speed
  slot_order:
  - Breastplate of Valor
  - Kinetic Cuirass
  - Bracer of The Abyss
  - Nimble Ring
  - Bragi's Harp
  - Gluttonous Grimoire
  flex_slots:
  - Bragi's Harp
  - Nimble Ring
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
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Basic-attack DPS skew (efficiency + fit + win/pick). Underrated for
    this god: Breastplate of Valor, Gluttonous Grimoire, Kinetic Cuirass, Amanita
    Charm, Oni Hunter''s Garb, Eye of Providence, Ethereal Staff, Soul Gem, Spectral
    Armor, Genji''s Guard, Shield of the Phoenix, Yogi''s Necklace, Freya''s Tears,
    Mantle Of Discord, Bracer of The Abyss, Shifter''s Shield, Bragi''s Harp, Death
    Metal, Wish-Granting Pearl, Jade Scepter, Erosion, Rod of Asclepius, Leviathan''s
    Hide, Draconic Scale, Nimble Ring, Bancroft''s Talon, Blood-Bound Book.'
  slot_scores:
    Breastplate of Valor:
      total: 0.55
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.21
    Kinetic Cuirass:
      total: 0.52
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.44
    Bracer of The Abyss:
      total: 0.48
      efficiency: 0.62
      win: 0.5
      pick: 0.0
      fit: 0.26
    Nimble Ring:
      total: 0.47
      efficiency: 0.55
      win: 0.5
      pick: 0.0
      fit: 0.32
    Bragi's Harp:
      total: 0.48
      efficiency: 0.53
      win: 0.5
      pick: 0.0
      fit: 0.46
    Gluttonous Grimoire:
      total: 0.53
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.37
  starter: *id001
- source: suggested
  archetype: cooldown
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Breastplate of Valor
  - Kinetic Cuirass
  - Shield of the Phoenix
  - Freya's Tears
  flex_slots:
  - Freya's Tears
  - Eye of Providence
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Amanita Charm — magical protection
    swap_item: Amanita Charm
  - vs_tag: physical_heavy
    swap: Spectral Armor — physical protection
    swap_item: Spectral Armor
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Ability-uptime skew — Cooldown Rate is a rate, not a reduction (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Kinetic Cuirass,
    Shield of the Phoenix, Genji''s Guard, Amanita Charm, Gluttonous Grimoire, Freya''s
    Tears, Soul Gem, Eye of Providence, Oni Hunter''s Garb, Ethereal Staff, Chandra''s
    Grace, Spectral Armor, Shifter''s Shield, Chronos'' Pendant, Mantle Of Discord,
    Gladiator''s Shield, Erosion, Yogi''s Necklace, Screeching Gargoyle, Draconic
    Scale, Wish-Granting Pearl, Jade Scepter, Death Metal, Leviathan''s Hide, Rod
    of Asclepius, Gem of Focus.'
  slot_scores:
    Eye of Providence:
      total: 0.52
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.45
    Genji's Guard:
      total: 0.53
      efficiency: 0.74
      win: 0.43
      pick: 0.15
      fit: 0.48
    Breastplate of Valor:
      total: 0.59
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.48
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.55
    Shield of the Phoenix:
      total: 0.53
      efficiency: 0.61
      win: 0.5
      pick: 0.0
      fit: 0.61
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.64
  starter: *id001
- source: suggested
  archetype: strength
  slot_order:
  - Berserker's Shield
  - Breastplate of Valor
  - Jotunn's Revenge
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Berserker's Shield
  - Runeforged Hammer
  situational_swaps:
  - vs_tag: heavy_cc
    swap: Mantle Of Discord — CC-immunity / cleanse
    swap_item: Mantle Of Discord
  - vs_tag: magic_heavy
    swap: Kinetic Cuirass — magical protection
    swap_item: Kinetic Cuirass
  - vs_tag: physical_heavy
    swap: Amanita Charm — physical protection
    swap_item: Amanita Charm
  - vs_tag: sustain
    swap: Contagion — anti-heal
    swap_item: Contagion
  rationale: 'Off-type Strength build — this kit scales on it (efficiency + fit +
    win/pick). Underrated for this god: Breastplate of Valor, Gluttonous Grimoire,
    The Crusher, Jotunn''s Revenge, Berserker''s Shield, Runeforged Hammer, Hydra''s
    Lament, Kinetic Cuirass, Amanita Charm, Eye of Providence, Lernaean Bow, Oni Hunter''s
    Garb, Soul Gem, Avenging Blade, Golden Blade, Shield Splitter, Ethereal Staff,
    Pharaoh''s Curse, Eye of the Storm, Death Metal, Spectral Armor, Genji''s Guard,
    Shield of the Phoenix, Freya''s Tears, Mantle Of Discord, Damaru, Shifter''s Shield,
    Yogi''s Necklace, The Reaper, Bragi''s Harp, Triton''s Conch, Wish-Granting Pearl,
    Erosion, Heartseeker, Arondight, Jade Scepter, Draconic Scale, Shogun''s Ofuda,
    Spear of the Magus.'
  slot_scores:
    Berserker's Shield:
      total: 0.53
      efficiency: 0.74
      win: 0.5
      pick: 0.0
      fit: 0.33
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.24
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.45
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.42
    Gluttonous Grimoire:
      total: 0.54
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.44
    The Crusher:
      total: 0.54
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.44
  starter: *id001
- source: suggested
  archetype: str-int
  slot_order:
  - Breastplate of Valor
  - Jotunn's Revenge
  - Kinetic Cuirass
  - Runeforged Hammer
  - Gluttonous Grimoire
  - The Crusher
  flex_slots:
  - Runeforged Hammer
  - Kinetic Cuirass
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
    swap: Divine Ruin — anti-heal
    swap_item: Divine Ruin
  rationale: 'Hybrid Strength + Intelligence — this kit scales on both (efficiency
    + fit + win/pick). Underrated for this god: Breastplate of Valor, Gluttonous Grimoire,
    Jotunn''s Revenge, The Crusher, Runeforged Hammer, Kinetic Cuirass, Amanita Charm,
    Hydra''s Lament, Berserker''s Shield, Soul Gem, Ethereal Staff, Eye of Providence,
    Oni Hunter''s Garb, Death Metal, Avenging Blade, Shield Splitter, Spectral Armor,
    Genji''s Guard, Shield of the Phoenix, Eye of the Storm, Wish-Granting Pearl,
    Freya''s Tears, Lernaean Bow, Jade Scepter, Mantle Of Discord, Spear of the Magus,
    Triton''s Conch, Shifter''s Shield, Rod of Asclepius, Pharaoh''s Curse, Golden
    Blade, Yogi''s Necklace, Erosion, Helm of Radiance, Damaru, The Reaper, Draconic
    Scale, The Cosmic Horror, Bragi''s Harp.'
  slot_scores:
    Breastplate of Valor:
      total: 0.56
      efficiency: 0.67
      win: 0.62
      pick: 0.14
      fit: 0.25
    Jotunn's Revenge:
      total: 0.53
      efficiency: 0.69
      win: 0.5
      pick: 0.0
      fit: 0.42
    Kinetic Cuirass:
      total: 0.53
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.5
    Runeforged Hammer:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.39
    Gluttonous Grimoire:
      total: 0.55
      efficiency: 0.71
      win: 0.5
      pick: 0.0
      fit: 0.53
    The Crusher:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.42
  starter: *id001
- source: suggested
  archetype: model
  slot_order:
  - Eye of Providence
  - Genji's Guard
  - Kinetic Cuirass
  - Oni Hunter's Garb
  - Freya's Tears
  - Amanita Charm
  flex_slots:
  - Oni Hunter's Garb
  - Freya's Tears
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
    Underrated for this god: Kinetic Cuirass, Amanita Charm, Eye of Providence, Gluttonous
    Grimoire, Genji''s Guard, Oni Hunter''s Garb, Shield of the Phoenix, Freya''s
    Tears, Shifter''s Shield, Ethereal Staff, Breastplate of Valor, Spectral Armor,
    Erosion, Mantle Of Discord, Soul Gem, Draconic Scale, Wish-Granting Pearl, Leviathan''s
    Hide, Jade Scepter, Yogi''s Necklace, Rod of Asclepius, Hussar''s Wings, Midgardian
    Mail, Helm of Radiance, Chandra''s Grace, Hide of the Nemean Lion, Gladiator''s
    Shield.'
  slot_scores:
    Eye of Providence:
      total: 0.55
      efficiency: 0.65
      win: 0.5
      pick: 0.0
      fit: 0.63
    Genji's Guard:
      total: 0.52
      efficiency: 0.74
      win: 0.43
      pick: 0.15
      fit: 0.39
    Kinetic Cuirass:
      total: 0.56
      efficiency: 0.64
      win: 0.5
      pick: 0.0
      fit: 0.73
    Oni Hunter's Garb:
      total: 0.53
      efficiency: 0.7
      win: 0.5
      pick: 0.0
      fit: 0.41
    Freya's Tears:
      total: 0.53
      efficiency: 0.59
      win: 0.5
      pick: 0.0
      fit: 0.62
    Amanita Charm:
      total: 0.56
      efficiency: 0.68
      win: 0.5
      pick: 0.0
      fit: 0.63
  starter: *id001
---
